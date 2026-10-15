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

## Latest list — 2026-10-15 00:19 UTC

New packages created between 2026-10-14 23:21 UTC and 2026-10-15 00:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-15T00-19-37-960773Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-14 23:31:22 | [HmacManager.StackExchangeRedis](https://www.nuget.org/packages/HmacManager.StackExchangeRedis) | 1.0.0 | Joshua Zillwood | Atomic, Redis-backed replay protection for HmacManager: every policy on the Dis… |
| 2026-10-14 23:38:54 | [SshSharp.IO.Abstractions](https://www.nuget.org/packages/SshSharp.IO.Abstractions) | 0.5.0 | zcsizmadia | An IFileSystem (System.IO.Abstractions) over SFTP (SshSharp): code written agai… |
| 2026-10-14 23:38:56 | [SshSharp.FileProviders](https://www.nuget.org/packages/SshSharp.FileProviders) | 0.5.0 | zcsizmadia | An IFileProvider over SFTP (SshSharp): serve files from an SSH server to ASP.NE… |
| 2026-10-15 00:00:26 | [TradeRouter.Net](https://www.nuget.org/packages/TradeRouter.Net) | 2.0.0 | Tyrone Omidi | High-performance .NET maritime shortest-path routing library on the Marnet netw… |
| 2026-10-15 00:09:42 | [TINS.Native.FFTW.osx-x64](https://www.nuget.org/packages/TINS.Native.FFTW.osx-x64) | 1.1.0 | Harald Bârzan | FFTW native runtime assets for TINS.Core on osx-x64. GPL-2.0-or-later -- adding… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
