> cutmaster-ai's GitHub account was suspended; hosting moved to Codeberg (Forgejo) under a new username. Push auth from this Win11 machine is still unresolved.

# cutmaster-ai — git hosting moved to Codeberg after GitHub suspension

## What happened
`cutmaster-ai`'s GitHub account was suspended. Hosting moved to **Codeberg** (a public Forgejo instance), new username `pcvaders`. `gh` CLI no longer applies to this repo — use `git` directly + the Codeberg web UI, or the `tea` CLI.

## Open problem
HTTPS push hangs on git-credential-manager's interactive browser prompt when run from a non-interactive agent shell. No Codeberg SSH key exists on this Win11 machine (likely lives on the user's Mac only). Push auth from Win11 is unresolved. <!-- secret-scan-ok -->

## Status
Open — remote repointed to Codeberg, but this machine can't push yet.

## Related
- [[forgejo-mirror]] — a DIFFERENT thing: that's a self-hosted Forgejo instance on Proxmox LXC 106 (`<lan-ip>`) mirroring GitHub repos for redundancy. This page is about Codeberg, a third-party-hosted public Forgejo instance used as the new primary remote after a GitHub suspension. Same underlying software (Forgejo), same `pcvaders` account naming convention, unrelated infrastructure — don't conflate the two.
