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

## Latest list — 2026-11-16 04:19 UTC

New packages created between 2026-11-16 03:21 UTC and 2026-11-16 04:19 UTC.

[Full CSV](data/new-nuget-packages-2026-11-16T04-19-47-386632Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-16 03:22:47 | [Jakar.Http](https://www.nuget.org/packages/Jakar.Http) | 10.1.0 | Tyler Stegmaier | An HttpClient-based requester (WebRequester) with retries, typed JSON bodies on… |
| 2026-11-16 03:22:47 | [Jakar.Users](https://www.nuget.org/packages/Jakar.Users) | 10.1.0 | Tyler Stegmaier | User, group, role and address models (Guid- and long-keyed), login requests, cl… |
| 2026-11-16 03:27:46 | [Jakar.Logging](https://www.nuget.org/packages/Jakar.Logging) | 10.1.0 | Tyler Stegmaier | Serilog and Microsoft.Extensions.Logging support: app logger options, a file lo… |
| 2026-11-16 03:28:02 | [Webority.Imaging.Avif](https://www.nuget.org/packages/Webority.Imaging.Avif) | 0.14.0 | Webority Technologies | Decodes AVIF images for Webority.Imaging through the dav1d AV1 decoder. |
| 2026-11-16 03:39:11 | [BusinessFeatures.Recaptchas](https://www.nuget.org/packages/BusinessFeatures.Recaptchas) | 9.0.0 | Linh Nguyen | Google reCAPTCHA token verification for .NET APIs: the IRecaptchaService contra… |
| 2026-11-16 03:51:08 | [RocketMQ.Client.Remoting](https://www.nuget.org/packages/RocketMQ.Client.Remoting) | 0.0.1 | RocketMQ.Client | Apache RocketMQ client for the classic remoting protocol |
| 2026-11-16 04:06:29 | [AltStreamLib](https://www.nuget.org/packages/AltStreamLib) | 0.4.34 | Macha Celeste | A C# wrapper for altstream.online API |
| 2026-11-16 04:10:35 | [Optionary](https://www.nuget.org/packages/Optionary) | 0.1.1 | David Driscoll,Rocket Surgeon… | Source-generated, reflection-free options binding and JSON Schema for .NET conf… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
