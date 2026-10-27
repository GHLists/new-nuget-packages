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

## Latest list — 2026-10-27 01:21 UTC

New packages created between 2026-10-27 00:20 UTC and 2026-10-27 01:21 UTC.

[Full CSV](data/new-nuget-packages-2026-10-27T01-21-28-462034Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-27 00:42:49 | [RecursiveAI.OneShader.Tool](https://www.nuget.org/packages/RecursiveAI.OneShader.Tool) | 1.1.0 | Recursive AI, LLC | The oneshader command line: compiles HLSL vertex, pixel and compute shaders to… |
| 2026-10-27 00:58:59 | [RytaMapper](https://www.nuget.org/packages/RytaMapper) | 1.1.0 | Ryan Tavan | A lightweight, reflection-based object mapper with an AutoMapper-style configur… |
| 2026-10-27 01:00:43 | [WolverineFx.Bobcat](https://www.nuget.org/packages/WolverineFx.Bobcat) | 6.55.0 | Jeremy D. Miller,Babu Annamal… | Given/When/Then helpers for specifying Wolverine handlers and event-sourced sli… |
| 2026-10-27 01:01:20 | [WolverineFx.Bobcat.EventModel](https://www.nuget.org/packages/WolverineFx.Bobcat.EventModel) | 6.55.0 | Jeremy D. Miller,Babu Annamal… | Writes WolverineFx.Bobcat specifications, and the spec project around them, fro… |
| 2026-10-27 01:06:39 | [nugetgo.github.com.inconshreveable.mousetrap](https://www.nuget.org/packages/nugetgo.github.com.inconshreveable.mousetrap) | 1.1.0 | go2cs conversion | unofficial go2cs C# conversion of github.com/inconshreveable/mousetrap v1.1.0,… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
