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

## Latest list — 2026-11-15 03:19 UTC

New packages created between 2026-11-15 02:20 UTC and 2026-11-15 03:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-15T03-19-21-025156Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-15 02:22:56 | [symbolist](https://www.nuget.org/packages/symbolist) | 1.0.0 | Zachary Aaron Combs | Symbiotic List Library |
| 2026-11-15 02:24:19 | [Laranet.AspNetCore.Validation](https://www.nuget.org/packages/Laranet.AspNetCore.Validation) | 0.3.0 | TheJavaZ | Optional FluentValidation endpoint filter integration for ASP.NET Core Minimal… |
| 2026-11-15 02:26:11 | [Soenneker.Calcom.Blazor](https://www.nuget.org/packages/Soenneker.Calcom.Blazor) | 11.0.1 | Jake Soenneker | A Blazor interop library for Cal.com scheduling embeds |
| 2026-11-15 02:48:11 | [SendMock.Testcontainers](https://www.nuget.org/packages/SendMock.Testcontainers) | 1.0.0 | MD. Shibbir Ahmed | Starts SendMock in Docker from a test and gives its SMTP, HTTP and provider add… |
| 2026-11-15 02:56:42 | [DotGame.AudioCodecs](https://www.nuget.org/packages/DotGame.AudioCodecs) | 1.0.0 | Hot Chai Games LLC | Opus, FLAC and WAV audio codecs for .NET, with no dependencies. Trim and AOT sa… |
| 2026-11-15 03:01:09 | [PinguApps.BlazorContentContracts](https://www.nuget.org/packages/PinguApps.BlazorContentContracts) | 1.0.0 | PinguApps | Annotations for Blazor component content contracts, including restricted fragme… |
| 2026-11-15 03:01:11 | [PinguApps.BlazorContentContracts.Analyzers](https://www.nuget.org/packages/PinguApps.BlazorContentContracts.Analyzers) | 1.0.0 | PinguApps | Build-time analyzers for Blazor content contracts, with original Razor diagnost… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
