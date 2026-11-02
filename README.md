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

## Latest list — 2026-11-02 21:21 UTC

New packages created between 2026-11-02 20:22 UTC and 2026-11-02 21:21 UTC.

[Full CSV](data/new-nuget-packages-2026-11-02T21-21-29-839545Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-02 20:38:52 | [BenScr.Resilience](https://www.nuget.org/packages/BenScr.Resilience) | 1.0.0 | Ben Schneider | Async retry policies with explicit exception selection, bounded fixed or expone… |
| 2026-11-02 20:39:13 | [BenScr.DelimitedText](https://www.nuget.org/packages/BenScr.DelimitedText) | 1.0.0 | Ben Schneider | Strict streaming CSV text readers and writers with explicit dialects, bounded r… |
| 2026-11-02 20:41:42 | [BenScr.Binary](https://www.nuget.org/packages/BenScr.Binary) | 1.0.0 | Ben Schneider | C++20 header-only bounded binary readers and writers with endian integers, IEEE… |
| 2026-11-02 20:46:50 | [BenScr.TextMatching](https://www.nuget.org/packages/BenScr.TextMatching) | 1.0.0 | Ben Schneider | Unicode scalar Levenshtein distance and bounded deterministic fuzzy matching wi… |
| 2026-11-02 20:47:09 | [BenScr.SemanticVersions](https://www.nuget.org/packages/BenScr.SemanticVersions) | 1.0.0 | Ben Schneider | Strict SemVer 2.0 parsing, numeric precedence without fixed-width limits, exact… |
| 2026-11-02 20:50:12 | [BenScr.Curves](https://www.nuget.org/packages/BenScr.Curves) | 1.0.0 | Ben Schneider | C++20 header-only easing, time-mapped cubic Bezier curves and owning scalar key… |
| 2026-11-02 20:55:43 | [BenScr.Ranges](https://www.nuget.org/packages/BenScr.Ranges) | 1.0.0 | Ben Schneider | Immutable inclusive Int64 intervals and normalized range sets with exact UInt12… |
| 2026-11-02 20:56:06 | [BenScr.Bitsets](https://www.nuget.org/packages/BenScr.Bitsets) | 1.0.0 | Ben Schneider | C++20 owning dynamic bitsets with bounded storage, set operations, safe shifts,… |
| 2026-11-02 21:11:42 | [AWS.Bedrock.MAG](https://www.nuget.org/packages/AWS.Bedrock.MAG) | 0.2.0-preview | Amazon Web Services | AWS backends for Microsoft's Agent Governance Toolkit: a Bedrock Guardrails pol… |
| 2026-11-02 21:12:47 | [VetCore.Anmv.RepMedVet](https://www.nuget.org/packages/VetCore.Anmv.RepMedVet) | 1.0.0 | VetCoreSolution | Une bibliothèque de DTO pour le fichier REPMEDVET.xml, référentiel des médicame… |
| 2026-11-02 21:14:32 | [Mawi](https://www.nuget.org/packages/Mawi) | 1.0.0 | Pyrami | A .NET MAUI UI framework that renders the whole interface into a single WebView… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
