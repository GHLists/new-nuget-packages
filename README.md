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

## Latest list — 2026-11-07 06:19 UTC

New packages created between 2026-11-07 05:19 UTC and 2026-11-07 06:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T06-19-34-848665Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 05:48:27 | [YHG.FastBF](https://www.nuget.org/packages/YHG.FastBF) | 1.0.0 | Naveen Ojha | A fast, lightweight, and modern binary serialization and buffer deserialization… |
| 2026-11-07 05:54:08 | [Smdn.IO.UsbHid.Providers.HidApiDotNet](https://www.nuget.org/packages/Smdn.IO.UsbHid.Providers.HidApiDotNet) | 1.0.0 | smdn | `Smdn.IO.UsbHid.Providers.HidApiDotNet` is a backend provider for [Smdn.IO.UsbH… |
| 2026-11-07 05:59:16 | [MarkdownRenderX.Avalonia.Mermaid](https://www.nuget.org/packages/MarkdownRenderX.Avalonia.Mermaid) | 12.1.3.8 | RYCBStudio | Renders ```mermaid fenced code blocks as native SVG diagrams in MarkdownRenderX… |
| 2026-11-07 06:00:22 | [OpenUsd.Rendering.Physics](https://www.nuget.org/packages/OpenUsd.Rendering.Physics) | 0.17.0-alpha | marcschier | Optional exact-step physics publication and atomic simulation recording for Ope… |
| 2026-11-07 06:04:48 | [Sevencat.OnnxSharp](https://www.nuget.org/packages/Sevencat.OnnxSharp) | 0.0.1 | Sevencat | Package Description |
| 2026-11-07 06:08:36 | [LIghtJUNction.OniOnline.Framework](https://www.nuget.org/packages/LIghtJUNction.OniOnline.Framework) | 0.4.0 | LIghtJUNction | Game-independent networking, gameplay contracts and synchronization framework f… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
