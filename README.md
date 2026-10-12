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

## Latest list — 2026-10-12 11:20 UTC

New packages created between 2026-10-12 10:20 UTC and 2026-10-12 11:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-12T11-20-25-310193Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-12 10:24:46 | [LunaticPanel.Package.Tool](https://www.nuget.org/packages/LunaticPanel.Package.Tool) | 0.1.3 | Maksim Shimshon | Lunatic Panel Development Tool for Plugins |
| 2026-10-12 10:29:31 | [AR51.Net](https://www.nuget.org/packages/AR51.Net) | 3.0.302 | AR 51 LTD | Connect a .NET application to an AR 51 motion capture system: live skeletons an… |
| 2026-10-12 10:31:38 | [Assay.Refactoring](https://www.nuget.org/packages/Assay.Refactoring) | 0.9.0 | Magne Moss Helleborg | Assay's refactoring engine — symbol-addressed rename and safe delete, analyzer… |
| 2026-10-12 10:39:02 | [Synvro.Modulus.Authorization.EntityFrameworkCore](https://www.nuget.org/packages/Synvro.Modulus.Authorization.EntityFrameworkCore) | 1.4.0 | synvro | EF Core persistence for Modulus authorization: permission grants, org hierarchy… |
| 2026-10-12 11:04:56 | [LanAgent.Terminal](https://www.nuget.org/packages/LanAgent.Terminal) | 1.0.2 | LanAgent | LanAgent terminal AI agent with Hyperlight microVM CodeAct execution for Window… |
| 2026-10-12 11:05:58 | [CodeBrix.VideoProcessing.Android.MitLicenseForever](https://www.nuget.org/packages/CodeBrix.VideoProcessing.Android.MitLicenseForever) | 1.0.285.663 | Jeremy Ellis | The Android engine for CodeBrix.VideoProcessing.Core: analyse media files, deco… |
| 2026-10-12 11:06:12 | [BbQ.ChatWidgets.Blazor](https://www.nuget.org/packages/BbQ.ChatWidgets.Blazor) | 1.1.0 | Jean Marc Mbouma | Blazor components library for BbQ Chat Widgets - provides reusable UI component… |
| 2026-10-12 11:06:13 | [BbQ.LlamaCpp](https://www.nuget.org/packages/BbQ.LlamaCpp) | 1.1.0 | Jean Marc Mbouma | Verified llama.cpp installer and supervised local runtime for schema-first BbQ.… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
