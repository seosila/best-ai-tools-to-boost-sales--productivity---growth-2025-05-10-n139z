# Tool logo asset mapping

Keep verified, locally stored product marks in this directory. Do not use a remote image URL, reconstruct a brand mark, or add an asset until its source and permitted use have been checked.

| Tool | Intended local path |
| --- | --- |
| ChatGPT | `assets/logos/chatgpt.svg` |
| Apollo.io | `assets/logos/apollo.svg` |
| Clay | `assets/logos/clay.svg` |
| Gong | `assets/logos/gong.svg` |
| HubSpot Sales Hub | `assets/logos/hubspot-sales-hub.svg` |
| Salesforce Agentforce Sales | `assets/logos/salesforce-agentforce-sales.svg` |

These assets are not present yet. Pages therefore render a neutral text fallback rather than a missing image or an unverified existing asset.

When a verified asset is added, place it in the shared `.tool-logo-frame` used by category cards and profile headers. Supply intrinsic `width` and `height` attributes (96 by 96 is the nominal source box), retain the frame dimensions, and let `object-fit: contain` preserve the asset's aspect ratio. Use `alt=""` when the adjacent card heading or profile H1 already identifies the product; use concise descriptive alternative text only when an image conveys information not present in nearby text.
