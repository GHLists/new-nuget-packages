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

## Latest list — 2026-11-19 23:20 UTC

New packages created between 2026-11-19 22:20 UTC and 2026-11-19 23:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-19T23-20-12-36407Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-19 22:25:28 | [SemanticVersions](https://www.nuget.org/packages/SemanticVersions) | 1.0.0 | vlt technology inc. | Parse, compare and match versions per the Semantic Versions specification (semv… |
| 2026-11-19 22:33:45 | [DirectoryIndexToHtml](https://www.nuget.org/packages/DirectoryIndexToHtml) | 11.2026.1119 | Andrei Ignat | Generate transactional directory index HTML pages. |
| 2026-11-19 22:34:21 | [Dloizides.Testing.AspNetCore](https://www.nuget.org/packages/Dloizides.Testing.AspNetCore) | 0.8.0 | DLoizides | A probe pack for ASP.NET Core test hosts (MGMT-PORT-1): /metrics and /health/*… |
| 2026-11-19 22:40:04 | [Graphs.NET](https://www.nuget.org/packages/Graphs.NET) | 0.1.0-alpha | RoGgY | A high-performance, zero-allocation, Native AOT-ready graph library for .NET 10… |
| 2026-11-19 22:40:47 | [Mindfire.RazorEmail](https://www.nuget.org/packages/Mindfire.RazorEmail) | 1.0.1 | Nate Zaugg | Culture-aware Razor email templates from the filesystem with a fluent MailKit s… |
| 2026-11-19 22:41:42 | [Mindfire.RazorEmail.Identity](https://www.nuget.org/packages/Mindfire.RazorEmail.Identity) | 1.0.1 | Nate Zaugg | ASP.NET Core Identity email sender that renders Mindfire.RazorEmail templates,… |
| 2026-11-19 22:52:34 | [akilin.ApiKit](https://www.nuget.org/packages/akilin.ApiKit) | 0.1.0 | akilin | Exception-based error model (codes, payloads, field errors, guards) for RFC 945… |
| 2026-11-19 22:52:36 | [akilin.ApiKit.TsTypeGenerator](https://www.nuget.org/packages/akilin.ApiKit.TsTypeGenerator) | 0.1.0 | akilin | dotnet tool generating TypeScript types (error codes, payloads, enums) from an… |
| 2026-11-19 22:52:36 | [akilin.ApiKit.AspNetCore](https://www.nuget.org/packages/akilin.ApiKit.AspNetCore) | 0.1.0 | akilin | ASP.NET Core integration for akilin.ApiKit: every non-2xx response becomes RFC… |
| 2026-11-19 22:52:37 | [akilin.ApiKit.Testing](https://www.nuget.org/packages/akilin.ApiKit.Testing) | 0.1.0 | akilin | AwesomeAssertions extensions for testing akilin.ApiKit APIs: assert kit excepti… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
