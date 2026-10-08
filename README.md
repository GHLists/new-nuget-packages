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

## Latest list — 2026-10-08 17:20 UTC

New packages created between 2026-10-08 16:21 UTC and 2026-10-08 17:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-08T17-20-48-45094Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-08 16:29:34 | [SubtitleToolkit](https://www.nuget.org/packages/SubtitleToolkit) | 1.0.3 | SubtitleToolkit Contributors | Lightweight, zero-dependency .NET library for parsing, converting, and time-shi… |
| 2026-10-08 16:40:32 | [Kapusch.PostHog.Android](https://www.nuget.org/packages/Kapusch.PostHog.Android) | 0.1.1 | Kapusch | Thin JNI interop for the official PostHog Android SDK with native disk persiste… |
| 2026-10-08 16:48:57 | [Kapusch.PostHog.iOS](https://www.nuget.org/packages/Kapusch.PostHog.iOS) | 0.1.0 | Kapusch | Thin interop for the official PostHog iOS SDK with native disk persistence. |
| 2026-10-08 17:10:14 | [EFCore.SchemaSync](https://www.nuget.org/packages/EFCore.SchemaSync) | 0.1.0 | Ross Slaney | Your EF model is your schema. Deploy an EF Core model directly to SQL Server wi… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
