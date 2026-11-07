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

## Latest list — 2026-11-07 03:20 UTC

New packages created between 2026-11-07 02:21 UTC and 2026-11-07 03:20 UTC.

[Full CSV](data/new-nuget-packages-2026-11-07T03-20-05-922977Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-07 02:34:28 | [PdfiumWrapper.runtime.linux-musl-x64](https://www.nuget.org/packages/PdfiumWrapper.runtime.linux-musl-x64) | 2.1.0 | Emmanuel Hameyie | Native PDFium runtime binaries for linux-musl-x64. Internal runtime package for… |
| 2026-11-07 02:40:54 | [KeelMatrix.RateSpec](https://www.nuget.org/packages/KeelMatrix.RateSpec) | 0.1.0 | KeelMatrix | Verify ASP.NET Core rate-limit bursts, rejection, and partition isolation with… |
| 2026-11-07 02:53:03 | [StbTrueTypeNext](https://www.nuget.org/packages/StbTrueTypeNext) | 1.0.0 | StbTrueTypeNextTeam | Safe fork of StbTrueTypeSharp |
| 2026-11-07 02:54:23 | [MarkupString.Web](https://www.nuget.org/packages/MarkupString.Web) | 2.27.0 | SharpMUSH | The browser side of MarkupString: one stylesheet for every class the HTML write… |
| 2026-11-07 02:54:31 | [ProWorks.Umbraco.AI.PageEvaluator.Automate](https://www.nuget.org/packages/ProWorks.Umbraco.AI.PageEvaluator.Automate) | 17.6.1 | ProWorks, Jason Prothero | Umbraco Automate "Evaluate Page" step for the ProWorks AI Page Evaluator: evalu… |
| 2026-11-07 02:54:52 | [ProWorks.Umbraco.AI.PageEvaluator.Deploy](https://www.nuget.org/packages/ProWorks.Umbraco.AI.PageEvaluator.Deploy) | 17.6.1 | ProWorks, Jason Prothero | Umbraco Deploy support for ProWorks AI Page Evaluator configurations: deploys e… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
