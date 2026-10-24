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

## Latest list — 2026-10-24 02:21 UTC

New packages created between 2026-10-24 01:21 UTC and 2026-10-24 02:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-24T02-21-27-343272Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-24 01:22:40 | [ADOExt.IQueryable](https://www.nuget.org/packages/ADOExt.IQueryable) | 4.0.0-rc | Kevin Jin | Add IQueryable extention for MagicEastern.ADOExt.Sql. |
| 2026-10-24 01:39:52 | [LANCommander.Interposer.Relay](https://www.nuget.org/packages/LANCommander.Interposer.Relay) | 1.3.0 | pathartl | Relay server for the LANCommander Interposer's network relay: carries games' LA… |
| 2026-10-24 01:41:21 | [Dotenvx.Primitives](https://www.nuget.org/packages/Dotenvx.Primitives) | 3.3.0.1 | Scott Motte (@motdotla), Davi… | Parse, encrypt, decrypt, keypair, keyring and related primitives for .env files… |
| 2026-10-24 01:41:22 | [Dotenvx.Providers](https://www.nuget.org/packages/Dotenvx.Providers) | 0.3.5.1 | Scott Motte (@motdotla), Davi… | Look up dotenvx private keys in .env.keys, the OS secret store, Dotenvx Armor,… |
| 2026-10-24 01:41:23 | [Dotenvx.Core](https://www.nuget.org/packages/Dotenvx.Core) | 2.35.0.1 | Scott Motte (@motdotla), Davi… | Load, parse, get and set .env values (including encrypted ones) from .NET code:… |
| 2026-10-24 01:41:24 | [Dotenvx.Configuration](https://www.nuget.org/packages/Dotenvx.Configuration) | 2.35.0.1 | Scott Motte (@motdotla), Davi… | Adds .env files, encrypted ones included, to Microsoft.Extensions.Configuration… |
| 2026-10-24 01:41:26 | [Dotenvx](https://www.nuget.org/packages/Dotenvx) | 2.35.0.1 | Scott Motte (@motdotla), Davi… | The dotenvx command-line tool for .NET: run any program with its .env files inj… |
| 2026-10-24 01:47:32 | [BigDog.TcpFlow](https://www.nuget.org/packages/BigDog.TcpFlow) | 1.0.0 | Rob Walker | Typed, NativeAOT-friendly messaging over TCP. Send plain C# classes between .NE… |
| 2026-10-24 02:07:00 | [CdCSharp.Pangea.Files](https://www.nuget.org/packages/CdCSharp.Pangea.Files) | 1.0.58 | CdCSharp | Working through files with CdCSharp.Pangea: a list filled by picker or by dropp… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
