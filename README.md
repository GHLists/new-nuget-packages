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

## Latest list — 2026-10-28 18:20 UTC

New packages created between 2026-10-28 17:19 UTC and 2026-10-28 18:20 UTC.

[Full CSV](data/new-nuget-packages-2026-10-28T18-20-36-953371Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-10-28 17:26:59 | [MASS4.Graph.Control](https://www.nuget.org/packages/MASS4.Graph.Control) | 1.0.0 | Bruno Massa | Control-flow semantics for MASS4.Graph: exec ports, deterministic ordering, ear… |
| 2026-10-28 17:27:00 | [MASS4.Graph.State](https://www.nuget.org/packages/MASS4.Graph.State) | 1.0.0 | Bruno Massa | State-machine semantics for MASS4.Graph: cyclic states, typed triggers, guarded… |
| 2026-10-28 17:27:01 | [MASS4.Graph.Dataflow](https://www.nuget.org/packages/MASS4.Graph.Dataflow) | 1.0.0 | Bruno Massa | Dataflow semantics for MASS4.Graph: pull evaluation, per-instance caching, acyc… |
| 2026-10-28 17:27:02 | [MASS4.Graph](https://www.nuget.org/packages/MASS4.Graph) | 1.0.0 | Bruno Massa | Headless, domain-neutral node-graph model: stable identity, reversible commands… |
| 2026-10-28 17:27:03 | [MASS4.Graph.Interpreter](https://www.nuget.org/packages/MASS4.Graph.Interpreter) | 1.0.0 | Bruno Massa | Reference backend for MASS4.Graph: interprets dataflow, control and state docum… |
| 2026-10-28 17:27:04 | [MASS4.Graph.Generator](https://www.nuget.org/packages/MASS4.Graph.Generator) | 1.0.0 | Bruno Massa | Compile-time graph registration and typed builders. |
| 2026-10-28 17:32:21 | [Soenneker.DataTables.Gen](https://www.nuget.org/packages/Soenneker.DataTables.Gen) | 11.0.1 | Jake Soenneker | Compile-time DataTables column mappings, permissions, and typed search expressi… |
| 2026-10-28 17:43:59 | [Arendi.Bluetooth.Hci.UserChannel](https://www.nuget.org/packages/Arendi.Bluetooth.Hci.UserChannel) | 19.5.0-beta1 | Arendi | Bluetooth Low Energy HCI transport for Linux Bluetooth controllers (hci0, hci1,… |
| 2026-10-28 17:44:01 | [Arendi.Bluetooth.BlueZ.Adapter](https://www.nuget.org/packages/Arendi.Bluetooth.BlueZ.Adapter) | 19.5.0-beta1 | Arendi | Bluetooth Low Energy Adapter for the Linux Bluetooth stack BlueZ (over D-Bus).… |
| 2026-10-28 17:52:27 | [Uneesoft.PaymentGateway.Sdk](https://www.nuget.org/packages/Uneesoft.PaymentGateway.Sdk) | 1.0.0 | Uneesoft | Official .NET SDK client for the Uneesoft Central Payment Gateway. |
| 2026-10-28 17:52:29 | [OpenAC.Net.Etq](https://www.nuget.org/packages/OpenAC.Net.Etq) | 1.0.0 | Projeto OpenAC .Net | Biblioteca multiplataforma para impressão de etiquetas PPLA, PPLB, EPL2, ZPL II… |
| 2026-10-28 17:54:53 | [OctoPublisher](https://www.nuget.org/packages/OctoPublisher) | 1.0.0 | octopublish | High-performance universal multi-store publishing CLI for modern CI/CD and loca… |
| 2026-10-28 17:55:17 | [VouchsafeClient](https://www.nuget.org/packages/VouchsafeClient) | 1.0.0 | Tuomas Hietanen | Vouchsafe identity verification API client: verifications, document checks, sma… |
| 2026-10-28 17:57:47 | [IpScope.Sdk](https://www.nuget.org/packages/IpScope.Sdk) | 1.0.0 | IPScope Engineering | Official zero-dependency, type-safe Sync & Async .NET Server-Side SDK for the I… |
| 2026-10-28 18:04:39 | [BancoBr.API](https://www.nuget.org/packages/BancoBr.API) | 1.0.0 | Adriano Trentim e colaborador… | Integração bancária por API para pagamentos, PIX, TED, DDA e extrato, conforme… |
| 2026-10-28 18:04:40 | [BancoBr.CNAB](https://www.nuget.org/packages/BancoBr.CNAB) | 1.0.0 | Adriano Trentim e colaborador… | Geração de remessas e leitura de retornos bancários CNAB 240 para pagamentos e… |
| 2026-10-28 18:04:40 | [BancoBr.Common](https://www.nuget.org/packages/BancoBr.Common) | 1.0.0 | Adriano Trentim e colaborador… | Tipos, enums e contratos compartilhados pelas integrações bancárias API e CNAB… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
