> TensorStack AmuseAI has no native pipeline for Gemini/Imagen/Veo — custom Python files reroute those model slots through Vertex AI (gcloud ADC), working as of 2026-06-11.

# AmuseAI — Google Vertex/GenAI pipeline integration

## Why
AmuseAI's built-in pipeline slots (`StableDiffusionPipeline`, `LatentConsistencyPipeline`) are ONNX-only — no native path to call Gemini/Imagen (image) or Veo (video). Custom `.py` files were dropped in to reroute those slots through Google's Vertex AI / GenAI SDK instead.

## Root cause hit + fixed
Early failures were traced to the UK region blocking the Gemini **free tier** API. Fix: pure gcloud ADC auth (`vertexai=True`, no API key) — same pattern as [[renderzero-vertex-patch]] on the Mac side. ADC sidesteps the free-tier regional block because it authenticates as a billed GCP project, not a free API key.

## Status
Closed / working as of 2026-06-11.

## Related
- [[renderzero-vertex-patch]] — same ADC-over-API-key pattern, ported cross-app <!-- secret-scan-ok -->
