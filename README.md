# New NuGet packages

Hourly lists of packages newly created on
[nuget.org](https://www.nuget.org/), built from the [v3 catalog](
https://api.nuget.org/v3/catalog0/index.json) of every package operation
nuget.org publishes. Each package touched in the window is checked against
its registration index, whose earliest `published` timestamp decides whether
the package was created inside the window.
A GitHub Actions workflow runs every hour, fetches the packages created since
the previous list and commits one CSV per run to [`data/`](data/), e.g.
[`data/new-nuget-packages-<timestamp>.csv`](data/).

Read the latest list below.

## Latest list — 2026-10-24 19:20 UTC

New packages created between 2026-10-24 18:20 UTC and 2026-10-24 19:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T19-20-52-558836Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 18:35:02 | [SLD.Serialization.Binary](https://www.nuget.org/packages/SLD.Serialization.Binary) | 2.3.18 | Andreas Hassmann | Simple serialization of object graphs |
| 2026-10-24 18:35:04 | [SLD.Serialization.Compression](https://www.nuget.org/packages/SLD.Serialization.Compression) | 2.3.18 | Andreas Hassmann | Wrapper around stdzstd compression implemented by |
| 2026-10-24 18:35:07 | [SLD.Serialization.Hash](https://www.nuget.org/packages/SLD.Serialization.Hash) | 2.3.18 | Crauzer, Andreas Hassmann | XXHash3 algorithm SLD namespacing fork of XXHash3.NET by Crauzer, adding streams |
| 2026-10-24 18:36:24 | [SLD.Generative.Code.Generator](https://www.nuget.org/packages/SLD.Generative.Code.Generator) | 1.0.31 | Andreas Hassmann | SLD Code Generation |
| 2026-10-24 18:36:27 | [SLD.Generative.MetaModel](https://www.nuget.org/packages/SLD.Generative.MetaModel) | 1.0.31 | Andreas Hassmann | SLD MetaModel |
| 2026-10-24 18:36:29 | [SLD.Generative.Model](https://www.nuget.org/packages/SLD.Generative.Model) | 1.0.31 | Andreas Hassmann | Code Generation for Models |
| 2026-10-24 18:39:25 | [Adamantium.Vulkan.ShaderObjectLayer](https://www.nuget.org/packages/Adamantium.Vulkan.ShaderObjectLayer) | 1.0.0 | Adamantium Studio | Khronos' VK_LAYER_KHRONOS_shader_object (Vulkan-ExtensionLayer), built for Wind… |
| 2026-10-24 19:00:49 | [AfrenAI.Mosaic](https://www.nuget.org/packages/AfrenAI.Mosaic) | 0.3.0 | AFREN AI | Bounded tool workflow execution with host-owned capability checks, protocol hos… |
| 2026-10-24 19:00:50 | [AfrenAI.Mosaic.Mcp](https://www.nuget.org/packages/AfrenAI.Mosaic.Mcp) | 0.3.0 | AFREN AI | MCP server tool adapter for the MOSAIC bounded workflow engine. |
| 2026-10-24 19:03:55 | [Newfoundcodes.Amaquet](https://www.nuget.org/packages/Newfoundcodes.Amaquet) | 0.1.0 | Newfoundcodes | Official .NET client SDK for the Amaquet data server, including native TCP/TLS… |
| 2026-10-24 19:06:33 | [CurlDotNet](https://www.nuget.org/packages/CurlDotNet) | 9.8.0 | Jacob Mellor,IronSoftware,Dan… | 🚀 THE KILLER FEATURE: Copy and paste any curl command - it just works! CurlDotN… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
