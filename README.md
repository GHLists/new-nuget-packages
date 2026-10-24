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

## Latest list — 2026-10-24 21:19 UTC

New packages created between 2026-10-24 20:19 UTC and 2026-10-24 21:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T21-19-18-258138Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 20:25:30 | [m2nj.MarkdownConverter](https://www.nuget.org/packages/m2nj.MarkdownConverter) | 1.0.0 | m2nj | A dependency-free .NET library for converting HTML to Markdown and Markdown to… |
| 2026-10-24 20:29:16 | [RootBlocks.AspNetCore.OpenApi](https://www.nuget.org/packages/RootBlocks.AspNetCore.OpenApi) | 0.5.0 | Sébastien de Salvador | OpenAPI document transformers (JSON Patch examples) for the built-in Microsoft.… |
| 2026-10-24 20:32:38 | [TextToVoice.Engines.Voxtral](https://www.nuget.org/packages/TextToVoice.Engines.Voxtral) | 0.3.0 | Robert Krogh | Voxtral (Mistral AI) engine for TextToVoice. Cloud-based TTS with streaming and… |
| 2026-10-24 21:12:12 | [E2E.WinApp.NUnit](https://www.nuget.org/packages/E2E.WinApp.NUnit) | 0.7.0 | hardkoded | WinAppTest for the E2E .NET port: a ready base class that launches a Windows de… |
| 2026-10-24 21:12:13 | [E2E.WinApp](https://www.nuget.org/packages/E2E.WinApp) | 0.7.0 | hardkoded | Windows app engine for the community .NET port of the e2e agentic testing frame… |
| 2026-10-24 21:12:16 | [E2E.WinApp.XUnit.V3](https://www.nuget.org/packages/E2E.WinApp.XUnit.V3) | 0.7.0 | hardkoded | WinAppTest for the E2E .NET port: a ready base class that launches a Windows de… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
