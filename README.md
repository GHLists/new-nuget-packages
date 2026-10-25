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

## Latest list — 2026-10-25 10:19 UTC

New packages created between 2026-10-25 09:19 UTC and 2026-10-25 10:19 UTC.

[Full CSV](data/new-nuget-packages-2026-10-25T10-19-37-69509Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-25 09:26:57 | [QuantumMatter.Application](https://www.nuget.org/packages/QuantumMatter.Application) | 1.0.0 | olgerd007 | Quantum simulation workflows, algorithms, terminal sampling and noisy trajector… |
| 2026-10-25 09:26:58 | [QuantumMatter.Core](https://www.nuget.org/packages/QuantumMatter.Core) | 1.0.0 | olgerd007 | Quantum circuit and state models, mathematical invariants, and backend extensio… |
| 2026-10-25 09:26:59 | [QuantumMatter.Infrastructure](https://www.nuget.org/packages/QuantumMatter.Infrastructure) | 1.0.0 | olgerd007 | Scalar CPU, parallel/SIMD CPU, NVIDIA CUDA and stochastic noise reference kerne… |
| 2026-10-25 09:29:53 | [StructuredDecisions.Base](https://www.nuget.org/packages/StructuredDecisions.Base) | 26.10.7239 | Curiosity GmbH, Convai Innova… | The shared base of the StructuredDecisions models: the decision-model interface… |
| 2026-10-25 09:29:56 | [StructuredDecisions.Laya.Catalyst](https://www.nuget.org/packages/StructuredDecisions.Laya.Catalyst) | 26.10.7239 | Curiosity GmbH, Convai Innova… | Statistical language identification for Laya's router, backed by Catalyst's lan… |
| 2026-10-25 09:29:59 | [StructuredDecisions.Laya.Training](https://www.nuget.org/packages/StructuredDecisions.Laya.Training) | 26.10.7239 | Curiosity GmbH, Convai Innova… | Fine-tuning for Laya decision checkpoints on the CPU: backpropagation through M… |
| 2026-10-25 09:30:03 | [StructuredDecisions.Laya](https://www.nuget.org/packages/StructuredDecisions.Laya) | 26.10.7239 | Curiosity GmbH, Convai Innova… | Laya: fast, non-autoregressive System 1 decisions with calibrated probabilities… |
| 2026-10-25 09:30:06 | [StructuredDecisions.Mica](https://www.nuget.org/packages/StructuredDecisions.Mica) | 26.10.7239 | Curiosity GmbH, Convai Innova… | Mica v0.5 4B on the CPU: a Qwen3.5 decoder (Gated DeltaNet + gated attention) t… |
| 2026-10-25 10:01:16 | [Synvro.Modulus.Testing.Authorization](https://www.nuget.org/packages/Synvro.Modulus.Testing.Authorization) | 1.6.0 | synvro | Conformance kit for an app's permission grants (TEST-1): the truth table every… |
| 2026-10-25 10:01:29 | [Synvro.Modulus.Secrets.OpenBao](https://www.nuget.org/packages/Synvro.Modulus.Secrets.OpenBao) | 1.6.0 | synvro | OpenBao (Vault-compatible) secret provider for Modulus: KV v2 reads and check-a… |
| 2026-10-25 10:12:45 | [SharpMediaInfo](https://www.nuget.org/packages/SharpMediaInfo) | 25.10.0 | Simone Bortolin | Package Description |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
