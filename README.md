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

## Latest list — 2026-10-22 02:21 UTC

New packages created between 2026-10-22 01:20 UTC and 2026-10-22 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-22T02-21-06-170302Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-22 01:29:23 | [OwlDomain.SDL3.Mixer.Native](https://www.nuget.org/packages/OwlDomain.SDL3.Mixer.Native) | 3.2.4 | OwlDomain | Native binaries for SDL3_mixer. |
| 2026-10-22 02:01:37 | [NuvTools.Security.Verification.Twilio](https://www.nuget.org/packages/NuvTools.Security.Verification.Twilio) | 10.0.0 | Nuv Tools | Twilio Verify implementation of the NuvTools.Security phone verification contra… |
| 2026-10-22 02:07:26 | [Icod.Dedit](https://www.nuget.org/packages/Icod.Dedit) | 1.0.0 | Timothy J. Bruce | Tabbed terminal text editor for .NET 8, 9 and 10. |
| 2026-10-22 02:11:04 | [PrintService.Core](https://www.nuget.org/packages/PrintService.Core) | 1.0.0 | Paicore | PrintService for ASP.NET Core |
| 2026-10-22 02:11:09 | [Fickl.AST](https://www.nuget.org/packages/Fickl.AST) | 0.5.2 | Alfonso García-Caro Núñez,Fab… | Fable AST |
| 2026-10-22 02:11:12 | [Fickl.Core](https://www.nuget.org/packages/Fickl.Core) | 0.5.2 | Alfonso García-Caro Núñez,Fab… | Fable Core Library |
| 2026-10-22 02:11:28 | [Fickl.Compiler](https://www.nuget.org/packages/Fickl.Compiler) | 0.5.2 | Alfonso García-Caro Núñez,Fab… | Package Description |
| 2026-10-22 02:14:17 | [Fickl.PublishUtils](https://www.nuget.org/packages/Fickl.PublishUtils) | 0.5.2 | Alfonso García-Caro Núñez,Fab… | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
