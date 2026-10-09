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

## Latest list — 2026-10-09 12:20 UTC

New packages created between 2026-10-09 11:19 UTC and 2026-10-09 12:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-09T12-20-03-053338Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-09 11:28:25 | [Speechwarp.Voice](https://www.nuget.org/packages/Speechwarp.Voice) | 0.3.7 | The speechwarp contributors | Text read aloud by Apple's voices (Eloquence and the rest) and sped up by speec… |
| 2026-10-09 11:36:06 | [Assertions.Web.Serializers.NewtonsoftJson](https://www.nuget.org/packages/Assertions.Web.Serializers.NewtonsoftJson) | 3.0.0 | Adrian Iftode | Newtonsoft.Json based serializer for FluentAssertions.Web, AwesomeAssertions.We… |
| 2026-10-09 11:41:21 | [Bexio.DotNet](https://www.nuget.org/packages/Bexio.DotNet) | 2.0.0 | Emanuel Mistretta | .NET client for the bexio API (2.0, 3.0 and 4.0) with personal access token and… |
| 2026-10-09 11:42:36 | [Avd.Price.Client](https://www.nuget.org/packages/Avd.Price.Client) | 0.0.1 | AVD | gRPC client and contracts for AVD Price & Catalog Service |
| 2026-10-09 11:53:23 | [BlockAuth.Sdk](https://www.nuget.org/packages/BlockAuth.Sdk) | 0.5.0 | Block-Auth.io Team | BlockAuth Auth SDK (.NET) — blockchain-based authentication client. |
| 2026-10-09 12:03:21 | [Audacia.UnitTest.Dependency](https://www.nuget.org/packages/Audacia.UnitTest.Dependency) | 1.0.0 | Audacia | A helper library for generating target classes. Install this NuGet package to e… |
| 2026-10-09 12:03:23 | [Audacia.UnitTest.Dependency.Azure](https://www.nuget.org/packages/Audacia.UnitTest.Dependency.Azure) | 1.0.0 | Audacia | A helper library for creating blueprints for Azure clients. Install this NuGet… |
| 2026-10-09 12:03:25 | [Audacia.UnitTest.Dependency.Http](https://www.nuget.org/packages/Audacia.UnitTest.Dependency.Http) | 1.0.0 | Audacia | A helper library for creating blueprints for HttpClient. Install this NuGet pac… |
| 2026-10-09 12:06:27 | [JoMo.CmdArgs](https://www.nuget.org/packages/JoMo.CmdArgs) | 1.0.0 | jmorgenroth | Simple C# command line argument interpreter |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
