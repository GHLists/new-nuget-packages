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

## Latest list — 2026-11-13 13:22 UTC

New packages created between 2026-11-13 12:19 UTC and 2026-11-13 13:22 UTC.

[Full CSV](data/new-nuget-packages-2026-11-13T13-22-57-340302Z.csv)

| Created (UTC) | Package | Version | Authors | Description |
| :------------ | :------ | :------ | :------ | :---------- |
| 2026-11-13 12:22:31 | [D365Solutions.WF2Flow.XrmToolBox](https://www.nuget.org/packages/D365Solutions.WF2Flow.XrmToolBox) | 1.2026.11.1 | D365 Solutions Ltd | Analyses Dynamics 365 / Dataverse background (asynchronous) classic workflows a… |
| 2026-11-13 12:23:54 | [FastTunnel.Hosting](https://www.nuget.org/packages/FastTunnel.Hosting) | 3.3.0 | Gui.H | expose a local server behind a NAT or firewall to the internet like ngrok and f… |
| 2026-11-13 12:34:29 | [Csag.Blueprint.Realtime.AzureSignalR](https://www.nuget.org/packages/Csag.Blueprint.Realtime.AzureSignalR) | 0.11.0 | collana solutions AG | Azure SignalR Service provider for the CSAG Blueprint real-time channel: tenant… |
| 2026-11-13 12:36:34 | [Medical.Fhir](https://www.nuget.org/packages/Medical.Fhir) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net FHIR R4 on the Firely .NET SDK: domain ↔ FHIR mapping (Patient, Enc… |
| 2026-11-13 12:36:34 | [Medical.Terminology](https://www.nuget.org/packages/Medical.Terminology) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net terminology services: SNOMED CT, ICD-10, LOINC and RxNorm lookup, b… |
| 2026-11-13 12:36:35 | [Medical.Native](https://www.nuget.org/packages/Medical.Native) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Native (Rust) high-performance kernels for Medical.Net — DICOM VOI window/level… |
| 2026-11-13 12:36:36 | [Medical.Core](https://www.nuget.org/packages/Medical.Core) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net core primitives: patient/encounter/observation domain model, clinic… |
| 2026-11-13 12:36:37 | [Medical.Emr](https://www.nuget.org/packages/Medical.Emr) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net EMR/EHR persistence on Entity Framework Core: patients, encounters,… |
| 2026-11-13 12:36:38 | [Medical.Templates](https://www.nuget.org/packages/Medical.Templates) | 1.0.0 | Gravicode Studios (Kang Fadhi… | dotnet new templates for Medical.Net: clinical console, FHIR R4 API server, HL7… |
| 2026-11-13 12:36:39 | [Medical.AI](https://www.nuget.org/packages/Medical.AI) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net AI: ML.NET clinical risk models (deterioration, type 2 diabetes) wi… |
| 2026-11-13 12:36:42 | [Medical.Cli](https://www.nuget.org/packages/Medical.Cli) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net command-line tool: clinical scores and calculators, terminology sea… |
| 2026-11-13 12:36:43 | [Medical.Dicom](https://www.nuget.org/packages/Medical.Dicom) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net DICOM on fo-dicom: metadata extraction, VOI window/level rendering… |
| 2026-11-13 12:36:44 | [Medical.Signals](https://www.nuget.org/packages/Medical.Signals) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net biosignals: synthetic ECG (normal sinus, tachycardia, bradycardia,… |
| 2026-11-13 12:36:45 | [Medical.Clinical](https://www.nuget.org/packages/Medical.Clinical) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net clinical calculators: NEWS2, qSOFA, SIRS, CURB-65, CHA2DS2-VASc, HA… |
| 2026-11-13 12:36:46 | [Medical.Visualization](https://www.nuget.org/packages/Medical.Visualization) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net visualization: dependency-free SVG charts for clinical data — ECG s… |
| 2026-11-13 12:36:47 | [Medical.Rules](https://www.nuget.org/packages/Medical.Rules) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net clinical decision support: NRules forward-chaining rules (NEWS2 esc… |
| 2026-11-13 12:36:48 | [Medical.AspNetCore](https://www.nuget.org/packages/Medical.AspNetCore) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net for ASP.NET Core: FHIR R4 REST facade (CRUD, search, transactions,… |
| 2026-11-13 12:36:49 | [Medical.Privacy](https://www.nuget.org/packages/Medical.Privacy) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net privacy: de-identification of free-text clinical notes (HIPAA Safe… |
| 2026-11-13 12:36:49 | [Medical.Hl7](https://www.nuget.org/packages/Medical.Hl7) | 1.0.0 | Gravicode Studios (Kang Fadhi… | Medical.Net HL7 v2 on NHapi: parse any version, build ADT^A01 / ORU^R01 (2.5.1)… |
| 2026-11-13 12:43:50 | [PackageBat](https://www.nuget.org/packages/PackageBat) | 0.1.0 | moonwalker1307 | Shows which APIs a dependency upgrade changes that your code actually uses, and… |
| 2026-11-13 12:44:05 | [Sa.Outbox.Redis](https://www.nuget.org/packages/Sa.Outbox.Redis) | 0.20.0 | dundich | Simple Outbox for Redis Streams (publishing and using messages) |
| 2026-11-13 12:46:05 | [Bitwarden.Server.Sdk.CryptoPrimitives](https://www.nuget.org/packages/Bitwarden.Server.Sdk.CryptoPrimitives) | 0.1.0 | Bitwarden Inc. | Cryptographic primitives built on System.Security.Cryptography. |
| 2026-11-13 13:01:58 | [Necto.OpenApi](https://www.nuget.org/packages/Necto.OpenApi) | 0.2.1 | Necto | OpenAPI UI for ASP.NET Core with a Roslyn source generator that maps response v… |

## Data source

Data comes from the [nuget.org APIs](https://learn.microsoft.com/nuget/api/
overview), operated by the .NET Foundation. Package metadata is provided by
the package authors. This project is not affiliated with or endorsed by
Microsoft or the .NET Foundation.
