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

## Latest list — 2026-10-09 01:19 UTC

New packages created between 2026-10-09 00:21 UTC and 2026-10-09 01:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T01-19-54-38469Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 00:27:25 | [NickStrupat.AsyncLock](https://www.nuget.org/packages/NickStrupat.AsyncLock) | 0.0.1 | Nick Strupat | A thread-safe, FIFO, allocation-free async lock for .NET, with a Roslyn analyze… |
| 2026-10-09 00:40:43 | [Webority.Imaging](https://www.nuget.org/packages/Webority.Imaging) | 0.1.0 | Webority Technologies | Decodes, encodes and processes images in JPEG, PNG, WebP, GIF, BMP and TIFF for… |
| 2026-10-09 00:44:59 | [RVM.TcgDex](https://www.nuget.org/packages/RVM.TcgDex) | 1.0.0 | Rafael Veneroso Morici | C# SDK for the TCGdex API (Pokémon TCG): cards, sets, series, prices and images… |
| 2026-10-09 00:46:30 | [FluentGwt.AspNetCore](https://www.nuget.org/packages/FluentGwt.AspNetCore) | 1.0.0 | Tommy Long | FluentGwt hosts for ASP.NET Core: the real entry point or a test composition, a… |
| 2026-10-09 00:46:30 | [FluentGwt.Http](https://www.nuget.org/packages/FluentGwt.Http) | 1.0.0 | Tommy Long | FluentGwt HTTP redirection: replace the primary handler of HttpClientFactory cl… |
| 2026-10-09 00:46:31 | [FluentGwt](https://www.nuget.org/packages/FluentGwt) | 1.0.0 | Tommy Long | Given/When/Then for .NET tests: chains that read as one expression, a ServiceFi… |
| 2026-10-09 00:46:32 | [FluentGwt.Bogus](https://www.nuget.org/packages/FluentGwt.Bogus) | 1.0.0 | Tommy Long | FluentGwt with Bogus: fixture.Fake and fixture.Random, seeded from the fixture… |
| 2026-10-09 00:46:33 | [FluentGwt.Moq](https://www.nuget.org/packages/FluentGwt.Moq) | 1.0.0 | Tommy Long | FluentGwt with Moq: Services.Stub<Service>() registers a mock that replaces eve… |
| 2026-10-09 00:46:33 | [FluentGwt.Xunit](https://www.nuget.org/packages/FluentGwt.Xunit) | 1.0.0 | Tommy Long | FluentGwt for xunit v3: the test cancellation token and identity, integration t… |
| 2026-10-09 00:59:00 | [MaksimShimshon.Mediator](https://www.nuget.org/packages/MaksimShimshon.Mediator) | 1.0.0 | MaksimShimshon.Mediator | Core Package for Lunatic Panel's PLugin |
| 2026-10-09 01:03:58 | [Shirubasoft.Aspire.Tailscale](https://www.nuget.org/packages/Shirubasoft.Aspire.Tailscale) | 1.0.0 | Shirubasoft | Expose Aspire resources privately on a Tailscale tailnet through sidecar contai… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
