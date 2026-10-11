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

## Latest list — 2026-10-11 15:19 UTC

New packages created between 2026-10-11 14:21 UTC and 2026-10-11 15:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-11T15-19-46-7001Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-11 14:40:47 | [Kreisverkehr.TsDecoder](https://www.nuget.org/packages/Kreisverkehr.TsDecoder) | 4.0.0-beta1 | Lewis Kirkaldie,Kreisverkehr | Unofficial fork of Cinegy.TsDecoder, an MPEG2 Transport Stream decoder for .NET… |
| 2026-10-11 14:44:02 | [Junexis.Studio.Platform.Binaries](https://www.nuget.org/packages/Junexis.Studio.Platform.Binaries) | 0.1.0 | Junexis | Prebuilt Junexis platform assemblies required by the public Junexis Studio repo… |
| 2026-10-11 14:46:53 | [FilexUI.CommunityToolkit.Mvvm.Extension.WPF](https://www.nuget.org/packages/FilexUI.CommunityToolkit.Mvvm.Extension.WPF) | 1.0.0 | wenke | 当前库是CommunityToolkit.Mvvm.Extension 的 WPF 版本，提供 Dialog、Module、Navigation 功能扩展 |
| 2026-10-11 14:49:29 | [metalTools.DiscoveryHost](https://www.nuget.org/packages/metalTools.DiscoveryHost) | 26.10.11.1 | Daniel T. Houck | Deploys the independent .NET 10 discovery host beside applications for automati… |
| 2026-10-11 14:50:27 | [LicenseChain.VB.SDK](https://www.nuget.org/packages/LicenseChain.VB.SDK) | 1.0.1 | LicenseChain Team | Official LicenseChain VB.NET SDK for license management and validation |
| 2026-10-11 14:59:42 | [Asgard.Heimdall.Client](https://www.nuget.org/packages/Asgard.Heimdall.Client) | 5.5.3 | BenLampson | Heimdall OAuth/PKCE, device authorization, JWT/opaque tokens, MCP authenticatio… |
| 2026-10-11 15:08:36 | [FilexUI.CommunityToolkit.Mvvm.Extension](https://www.nuget.org/packages/FilexUI.CommunityToolkit.Mvvm.Extension) | 1.0.0 | wenke | 当前库是CommunityToolkit.Mvvm的核心扩展包，提供 Dialog、Module、Navigation 插件 |
| 2026-10-11 15:08:42 | [Jadi.Framework.Utilities](https://www.nuget.org/packages/Jadi.Framework.Utilities) | 1.0.1 | Jadi AB | General purpose utilities, extension methods, collections and helpers. |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
