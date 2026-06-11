# RenderZero Vertex AI Patch (Studio + Animate)

Reroutes RenderZero's Gemini / Nano Banana / Veo generation through **Vertex AI (gcloud ADC)** instead of the API key path. Reference doc for porting the Mac patch to Windows 11.

> Placeholders: replace `YOUR_PROJECT` with your GCP project id and `YOUR_ACCOUNT` with your Google account. Do not commit real values.

## Apps
RenderZero Studio.app + RenderZero Animate.app — Electron apps. On Mac: `/Applications/1AI_Robotics/`. On Win 11: `%LOCALAPPDATA%\Programs\` or wherever the installer placed them; the `resources/app.asar` is the patch target.

## Auth foundation (gcloud ADC — no API key)
```bash
gcloud auth login
gcloud auth application-default login
gcloud auth application-default set-quota-project YOUR_PROJECT
```
- Vertex API (`aiplatform.googleapis.com`) must be enabled on the project.
- Runtime dep: `gcloud auth print-access-token` must succeed.
- Unset `GEMINI_API_KEY` / `GOOGLE_API_KEY` so the Vertex path wins.
- **Windows note:** set env vars at the OS level (System Properties → Environment Variables), not just the shell — Electron GUI app won't inherit a shell session. ADC file lands at `%APPDATA%\gcloud\application_default_credentials.json`.

## The patch — 3 asar edits
1. `electron/preload.cjs` — add to contextBridge:
   `getVertexCredentials: () => ipcRenderer.invoke('get-vertex-credentials')`
2. `electron/main.cjs` — add `runGcloud()` + `ipcMain.handle('get-vertex-credentials')` returning gcloud token + project. Insert before the `http-fetch` handler.
   - **Windows note:** `runGcloud()` must call `gcloud.cmd` (not bare `gcloud`) via the absolute install path, e.g. `C:\Users\YOU\AppData\Local\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd`. Spawn with `shell:true` or resolve `.cmd` explicitly.
3. Renderer chunk — rewrite Gemini `generateImage` / `editImage`: try Vertex first (`window.electron.getVertexCredentials()` + fetch to the Vertex endpoint), fall back to original SDK path.
   - Studio chunk: `dist/assets/index-qnDlBIc2.js`
   - Animate chunk: `dist/assets/provider-runtime-DNwHugSi.js` (split build; index has no Gemini SDK)

## Keyless gate (required, or gen is blocked before Vertex runs)
Gemini provider `getApiKey()` throws and `checkApiKey()` is false when no key stored → app shows "set up in API settings" and blocks BEFORE the Vertex branch. Patch:
- `getApiKey`: `if(!t)throw...` → `if(!t)return "vertex-ai-managed"`
- `checkApiKey(){...hasSelectedApiKey()...}` → `checkApiKey(){return true}`

## CRITICAL — model ids + region (wrong values = 404)
- nano-banana-2 = `gemini-3.1-flash-image-preview`
- nano-banana-pro = `gemini-3-pro-image-preview`
- These live at location **`global`** → host `aiplatform.googleapis.com` (NO regional prefix).
- **KEEP the `-preview` suffix.** Stripping it or using `us-central1` → 404 NOT_FOUND → swallowed by fallback → app shows "API key invalid/expired/revoked/missing".
- `gemini-2.5-flash-image` (original Nano Banana) works in `us-central1`; the gemini-3.x models do NOT.
- Host should be conditional: `creds.location==="global" ? "aiplatform.googleapis.com" : creds.location+"-aiplatform.googleapis.com"`.

## Video (Veo) — separate from image
- Animate Veo chunk: `dist/assets/video-adapters-C1aBiAev.js`. Studio: same `index-qnDlBIc2.js` (single build, no separate video chunk).
- Preview ids `veo-3.1-generate-preview` / `veo-3.1-fast-generate-preview` → **404 on Vertex**. Map to GA: `veo-3.1-generate-001` / `veo-3.1-fast-generate-001` (both verified 200 + mp4).
- Vertex Veo flow: build `{instances:[{prompt,image?,lastFrame?,referenceImages?}],parameters:{sampleCount,durationSeconds,resolution,aspectRatio,seed?,negativePrompt?,personGeneration}}` → POST `:predictLongRunning` → poll `:fetchPredictOperation` (`{operationName}`) until `done` → extract `response.videos[0].bytesBase64Encoded` → data URL.
- SDK image field `{imageBytes}` → Vertex `{bytesBase64Encoded}`.
- On creds-present Vertex failure: THROW the real error (no silent SDK fallback). Only fall back to SDK when creds missing.

## asar repack gotchas (these brick the app if wrong)
- Payload base = `16 + json_size + pad`, where `pad = (4 - (json_size % 4)) % 4`. Using `16 + json_size` corrupts every file by `pad` bytes.
- `ElectronAsarIntegrity` hash in the app manifest = sha256 of the **JSON header only**, NOT the whole file.
  - **Windows note:** Electron's asar integrity check exists on Win too, but the manifest location differs — it's in the PE/resource config, not an Info.plist. Verify whether the Windows build enforces integrity; if it does, recompute the header hash there.
- Every file carries a per-file `integrity` block (SHA256 + 4MiB chunks). Recompute for modified files on repack.

## Deploy
Mac: kill app → swap `app.asar` → set header hash in Info.plist → `xattr -cr` → `codesign -s - --deep --force` → verify.
**Windows:** kill app → swap `resources\app.asar` → no codesign step (unless the build is signed; ad-hoc re-sign not available the same way) → relaunch. If the app refuses to load (integrity), the manifest hash must be updated for the Win build.

## Porting checklist (Mac → Win 11)
1. Install Google Cloud SDK for Windows; confirm `gcloud auth print-access-token` works.
2. Run the ADC login commands above; set env vars at OS level.
3. Locate `resources\app.asar` inside the Windows install dir.
4. Apply the same 3 asar edits + keyless gate. Use `gcloud.cmd` absolute path in `runGcloud()`.
5. Use the **global** region + **-preview** model ids (image), GA `-001` ids (Veo).
6. Repack with correct padding + per-file integrity; update manifest hash if Win build enforces it.
7. Test direct Vertex curl first (global + `gemini-3-pro-image-preview` → expect 200 + PNG) before blaming the patch.
