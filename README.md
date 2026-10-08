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

## Latest list — 2026-10-08 12:22 UTC

New packages created between 2026-10-08 11:19 UTC and 2026-10-08 12:22 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T12-22-15-208514Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 11:22:33 | [mimic-browser.Playwright](https://www.nuget.org/packages/mimic-browser.Playwright) | 0.1.0 | Mimic.Playwright | Package Description |
| 2026-10-08 11:28:00 | [mimic-browser.PuppeteerSharp](https://www.nuget.org/packages/mimic-browser.PuppeteerSharp) | 0.1.0 | Mimic.PuppeteerSharp | Package Description |
| 2026-10-08 11:31:16 | [E2E.XUnit.V3](https://www.nuget.org/packages/E2E.XUnit.V3) | 0.2.0 | hardkoded | xUnit v3 fixture for the E2E .NET port. Each test gets an engine session, and t… |
| 2026-10-08 11:31:32 | [GonFox.GameBoy.Platform.Android](https://www.nuget.org/packages/GonFox.GameBoy.Platform.Android) | 1.0.0 | machi_pon | Android host support for GonFox.GameBoy (AudioTrack output, storage, haptics, r… |
| 2026-10-08 11:31:33 | [GonFox.GameBoy.Platform.Windows](https://www.nuget.org/packages/GonFox.GameBoy.Platform.Windows) | 1.0.0 | machi_pon | Windows host support for GonFox.GameBoy (WASAPI audio output, storage, settings) |
| 2026-10-08 11:31:34 | [GonFox.GameBoy.Core](https://www.nuget.org/packages/GonFox.GameBoy.Core) | 1.0.0 | machi_pon | Game Boy (DMG) emulator core |
| 2026-10-08 11:31:35 | [GonFox.GameBoy.Platform.Shared](https://www.nuget.org/packages/GonFox.GameBoy.Platform.Shared) | 1.0.0 | machi_pon | Platform-neutral host support for GonFox.GameBoy (run thread, session, frames,… |
| 2026-10-08 11:44:01 | [SuperScrapers.Contracts](https://www.nuget.org/packages/SuperScrapers.Contracts) | 1.3.11 | Appliman | Public requests, responses and contracts for the SuperScrapers network. |
| 2026-10-08 11:44:02 | [SuperScrapers.Client](https://www.nuget.org/packages/SuperScrapers.Client) | 1.3.11 | Appliman | Typed client for the SuperScrapers network. |
| 2026-10-08 11:46:48 | [ThrottleDebounce.SourceGenerators](https://www.nuget.org/packages/ThrottleDebounce.SourceGenerators) | 1.0.2 | Carlos | Prism MVVM ThrottleDebounceCommandGenerator |
| 2026-10-08 11:47:48 | [DotNetBrowser.AgentSkills](https://www.nuget.org/packages/DotNetBrowser.AgentSkills) | 4.3.3 | TeamDev Ltd. | The DotNetBrowser agent skill for AI coding agents such as Claude Code, Codex,… |
| 2026-10-08 11:50:20 | [MonoGame.Runtime.Linux.DesktopGL4](https://www.nuget.org/packages/MonoGame.Runtime.Linux.DesktopGL4) | 3.8.6 | MonoGame Team | Package Description |
| 2026-10-08 11:50:26 | [MonoGame.Runtime.Windows.DesktopGL4](https://www.nuget.org/packages/MonoGame.Runtime.Windows.DesktopGL4) | 3.8.6 | MonoGame Team | Package Description |
| 2026-10-08 11:50:29 | [MonoGame.Runtime.Mac.DesktopGL4](https://www.nuget.org/packages/MonoGame.Runtime.Mac.DesktopGL4) | 3.8.6 | MonoGame Team | Package Description |
| 2026-10-08 11:56:25 | [Autodesk.Revit.Sdk.Refs.2027](https://www.nuget.org/packages/Autodesk.Revit.Sdk.Refs.2027) | 2.0.0 | dosymep | The Software Development Toolkit (SDK) provides extensive .NET code samples and… |
| 2026-10-08 12:00:14 | [Delibera.Redis](https://www.nuget.org/packages/Delibera.Redis) | 10.5.1 | Victor Buzin | Redis-backed distributed debate execution for the Delibera multi-model AI counc… |
| 2026-10-08 12:00:15 | [Delibera.Server](https://www.nuget.org/packages/Delibera.Server) | 10.5.1 | Victor Buzin | ASP.NET Core host for the Delibera multi-model AI council framework: debate, sc… |
| 2026-10-08 12:10:12 | [PANiXiDA.Core.Infrastructure.Storage.S3](https://www.nuget.org/packages/PANiXiDA.Core.Infrastructure.Storage.S3) | 1.0.2 | PANiXiDA | S3-compatible file storage adapter for PANiXiDA.Core applications, providing up… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
