# Review-comment patterns — what your code reviews look like

Based on **466 review comments** authored across **187 PRs**.

This file shows the kinds of feedback you give in code review. Themes drawn from the actual comment text are interleaved with concrete examples.

## Themes in your reviews (rough keyword distribution)

These are heuristic counts based on keyword matches in your comment text. Treat as a rough indicator of what you focus on.

| Theme | Comments mentioning |
|---|---:|
| TypeScript typing | 111 (23%) |
| React patterns | 18 (3%) |
| Styling / CSS | 21 (4%) |
| Lint / format | 37 (7%) |
| Naming / convention | 32 (6%) |
| Tracking / analytics | 15 (3%) |
| Security / safety | 5 (1%) |
| Performance | 14 (3%) |
| Suggestions / nitpicks | 132 (28%) |
| Bugs / corrections | 19 (4%) |
| Refactoring | 13 (2%) |
| Tests | 25 (5%) |

## Comment-length distribution

How verbose your reviews are. (Length here is approximate — multi-line bodies are joined with `\n`.)

| Length (chars) | Count | Note |
|---|---:|---|
| < 50 | 156 | Short nits / one-liners |
| 50–150 | 207 | Concise feedback |
| 150–300 | 79 | Substantive but focused |
| 300–600 | 21 | Detailed explanations |
| 600+ | 3 | Long-form / architectural |

**Median comment length:** 78 chars  
**Mean:** 107 chars  
**Max:** 1207 chars

## Sample comments by year (the actual text)

A small sample of your actual review comments per year. These show your tone, focus, and depth at different career stages.

### Year 1 (70 comments total)

**2021-05-06** — reviewing a teammate's PR [Freshview/createsend.com#9661](https://git.campmon.com/Freshview/createsend.com/pull/9661#discussion_r81905)
_File: `srcfrontend/app/audience/components/Lists/ConfirmBulkDeleteModal.tsx`_

> dialogue headers use `cmds-typography-subtitle`

**2021-06-16** — reviewing a teammate's PR [Freshview/createsend.com#10037](https://git.campmon.com/Freshview/createsend.com/pull/10037#discussion_r84392)
_File: `srcfrontend/app/automation/components/CopyDialog/CopyDialog.spec.tsx`_

> Should `await` the `waitFor` call. 

**2021-07-30** — reviewing a teammate's PR [Freshview/createsend.com#10033](https://git.campmon.com/Freshview/createsend.com/pull/10033#discussion_r86749)
_File: `app/js/src/app/contacts/hostedsubscribeform/components/Checkbox/index.tsx`_

> Fix `app/js/src/app/contacts/hostedsubscribeform/components/PrivacyBlock/PrivacyBlock.tsx` importing and using the wrong type `CheckboxProps` 

**2021-09-22** — reviewing a teammate's PR [Freshview/createsend.com#10950](https://git.campmon.com/Freshview/createsend.com/pull/10950#discussion_r89391)
_File: `srcfrontend/app/campaigncreationchecklist/components/CheckListSteps/ToStep/RecipientSelectionDialog/useDynamicContentRecipients.ts`_

> Type on `segment` to keep it consistent with the rest. 

**2022-03-29** — reviewing a teammate's PR [Freshview/createsend.com#12522](https://git.campmon.com/Freshview/createsend.com/pull/12522#discussion_r99035)
_File: `srcfrontend/app/smscampaigncreationchecklist/components/SmsMessageStep/SmsMessageArea.scss`_

> Check whitespace 

### Year 2 (97 comments total)

**2022-04-07** — reviewing a teammate's PR [Freshview/createsend.com#12587](https://git.campmon.com/Freshview/createsend.com/pull/12587#discussion_r99647)
_File: `srcfrontend/app/clientsettings/components/AnalyticsAndApi/ApiKeyColumn.tsx`_

> This reads like it should be an object destructure
> ```
> const {_errors} = json;
> ```

**2022-07-05** — reviewing a teammate's PR [platform/kafka-acls#89](https://git.campmon.com/platform/kafka-acls/pull/89#discussion_r104228)
_File: `topics.json`_

> ```suggestion
>     "consumers": [ "InsightsKafkaConsumer" ],
> ```

**2022-09-05** — reviewing a teammate's PR [Freshview/createsend.com#13543](https://git.campmon.com/Freshview/createsend.com/pull/13543#discussion_r107169)
_File: `srcfrontend/app/campaignreport/components/Snapshot/MachineClicksBanner/MachineClicksBanner.tsx`_

> I don't mind. 
> Usually there's something upstream to catch this and display a toast or some error state. 
> Guess it doesn't hurt to not rethrow either at this stage. 

**2022-10-13** — reviewing a teammate's PR [Freshview/createsend.com#13796](https://git.campmon.com/Freshview/createsend.com/pull/13796#discussion_r109235)
_File: `srcfrontend/app/smscampaigncreationchecklist/components/SmsMessageStep/SmsComplianceToggles/SmsComplianceToggles.tsx`_

> This is a no-op event handler. 
> Recommend getting rid of this, and modify the Toggle component to optionally take in handlers instead. 

**2023-03-28** — reviewing a teammate's PR [Freshview/createsend.com#14950](https://git.campmon.com/Freshview/createsend.com/pull/14950#discussion_r116914)
_File: `shared/components/managecard/Card/AddCardComponents/CardHostedFields.tsx`_

> Can move the below code into a helper function to preserve const-ness here.
> 
> This does not look like it needs to be recomputed on every render. 
> Can consider moving the variable assignment inside `setCardNumberValidationState()` 
> 
> 

### Year 3 (112 comments total)

**2023-06-02** — reviewing a teammate's PR [Freshview/createsend.com#15447](https://git.campmon.com/Freshview/createsend.com/pull/15447#discussion_r120020)
_File: `srcfrontend/app/audience/components/CustomFields/CustomFieldsDraggableTableRow.tsx`_

> nit: don't have to default false.

**2023-08-10** — reviewing a teammate's PR [Freshview/createsend.com#15918](https://git.campmon.com/Freshview/createsend.com/pull/15918#discussion_r123918)
_File: `srcfrontend/app/commercesettings/pages/ShopifyMigrationStatusAgency/LegacyShopifyIntegrationContextProvider.tsx`_

> Thoughts? 
> 
> ```suggestion
>                         .filter((legacy) => Boolean(listImportStatusMap[legacy.clientId]))
> ```

**2023-08-25** — reviewing a teammate's PR [Engineering/SegmentTrackingPlan#420](https://git.campmon.com/Engineering/SegmentTrackingPlan/pull/420#discussion_r124806)
_File: `TrackingPlan/events.yaml`_

> Tracking Plan Uses Pascal Case
> ```suggestion
>           - Non-Human Click Filter
> ```

**2023-09-22** — reviewing a teammate's PR [Freshview/createsend.com#16256](https://git.campmon.com/Freshview/createsend.com/pull/16256#discussion_r126292)
_File: `srcfrontend/app/automation/components/CreateWorkflowFromRecipe/CreateCommerceWorkflow.tsx`_

> Suggestion: `hasRequiredSegmentsForRecipe` 

**2024-03-13** — reviewing a teammate's PR [Freshview/createsend.com#17201](https://git.campmon.com/Freshview/createsend.com/pull/17201#discussion_r132766)
_File: `srcfrontend/app/twofactormemberstatus/components/TwoFactorMemberStatus/utils.ts`_

> They can be different. 
> 
> Button texts go with the cmds guideline https://cmds.campmon.com/#/writing/capitalization
> Analytics properties go with the segments taxonomy guideline https://git.campmon.com/Engineering/SegmentTrackingPlan/wiki/Taxonomy-Guidelines

### Year 4 (45 comments total)

**2024-04-09** — reviewing a teammate's PR [Engineering/contentbuildercontext.staticresourceservice.core#1004](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1004#discussion_r133426)
_File: `ContentBuilderContext.StaticResourceService/static_src/ts/modules/emailbuilder/services/live-content-enablement.service.ts`_

> TODO?

**2024-06-25** — reviewing a teammate's PR [Engineering/workflowbuildercontext.uiservice.core#241](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/241#discussion_r135608)
_File: `WorkflowBuilderContext.UIService/ui/components/CustomField/components/CustomFieldExpressionSyntaxElement.tsx`_

> Nit: `i` is not used. Also avoid single character variable names pls

**2024-08-06** — reviewing a teammate's PR [Engineering/workflowbuildercontext.uiservice.core#264](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/264#discussion_r136902)
_File: `WorkflowBuilderContext.UIService/ui/components/CustomField/CustomFieldDetails.tsx`_

> `resetValidation` is always set when you connect the component (`validateForm()`) at the bottom of the file. 
> 
> Shouldn't need to mark it as optional `?` 
> 
> Unless I am missing something?

**2024-10-24** — reviewing a teammate's PR [Engineering/contentbuildercontext.staticresourceservice.core#1078](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1078#discussion_r138862)
_File: `ContentBuilderContext.StaticResourceService/static_src/scss/components/toolbar/_toolbar-padding.scss`_

> There's a space here 🤔 
> It's a line with one space ` ` character.

**2025-03-28** — reviewing a teammate's PR [Engineering/workflowbuildercontext.uiservice.core#288](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/288#discussion_r143366)
_File: `WorkflowBuilderContext.UIService/ui/components/Step/AddStep.tsx`_

> Interesting stub 😄 

### Year 5 (130 comments total)

**2025-05-08** — reviewing a teammate's PR [Freshview/createsend.com#19679](https://git.campmon.com/Freshview/createsend.com/pull/19679#discussion_r144743)
_File: `extras/CampMon.ServiceAgents.NetCore/CampMon.WorkflowCloneAgent/Services/WorkflowCloneCreationService.cs`_

> Maybe consider 
> ```suggestion
>                     throw new ArgumentOutOfRangeException(nameof(sourceStep.Type));
> ```
> 

**2025-10-28** — reviewing a teammate's PR [Freshview/createsend.com#21066](https://git.campmon.com/Freshview/createsend.com/pull/21066#discussion_r152919)
_File: `srcfrontend/app/clientoverview/components/FoundationalSteps/FoundationalStepCardStatusLozenge.tsx`_

> ```suggestion
> const Skipped = () => {
> ```

**2025-11-13** — reviewing a teammate's PR [Engineering/contentbuildercontext.staticresourceservice.core#1131](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1131#discussion_r154109)
_File: `ContentBuilderContext.StaticResourceService/static_src/ts/modules/emailbuilder/services/rfc6902-patch.service.ts`_

> Woah it's jquery!! 

**2026-01-30** — reviewing a teammate's PR [Freshview/createsend.com#22070](https://git.campmon.com/Freshview/createsend.com/pull/22070#discussion_r159369)
_File: `app/CampMon.CmAPI/Endpoints/CrmLite/Models/CmCrmCustomerDetails.cs`_

> ```
> Action GetCrmCustomerDetails on controller CrmLiteController includes a DateTime property in the response type System.Threading.Tasks.Task`1[Microsoft.AspNetCore.Mvc.ActionResult~1[CampMon.CmAPI.Endpoints.CrmLite.Models.CmCrmCustomerDetails]] 
> 
> ```
> 
> Should be returning `string` in cmapi models. 
> You can probably just `.ToString("o")` the DateTime value. (Check with csharp crew)

**2026-03-27** — reviewing a teammate's PR [Freshview/createsend.com#22683](https://git.campmon.com/Freshview/createsend.com/pull/22683#discussion_r163126)
_File: `srcfrontend/app/audience/components/SubscriberProfile/SegmentMembershipModal.tsx`_

> Use https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/localeCompare

### Year 6 (12 comments total)

**2026-04-13** — reviewing a teammate's PR [Freshview/createsend.com#22766](https://git.campmon.com/Freshview/createsend.com/pull/22766#discussion_r164274)
_File: `srcfrontend/app/audience/components/CrmLite/CrmOptInUpsell/CrmOptInUpsell.tsx`_

> Don't need this React.Fragment

**2026-04-16** — reviewing a teammate's PR [Freshview/createsend.com#22873](https://git.campmon.com/Freshview/createsend.com/pull/22873#discussion_r164570)
_File: `app/CampMon.CmAPI/Endpoints/Sequence/SequenceAddCampaignValidator.cs`_

> TODO

**2026-04-21** — reviewing a teammate's PR [Freshview/createsend.com#22903](https://git.campmon.com/Freshview/createsend.com/pull/22903#discussion_r164942)
_File: `srcfrontend/app/audience/components/CrmLite/CrmLiteApi.ts`_

> Do you need to explicitly check for `false` here? 
> If not it's better written as 
> ```
> if (!result.hasCrmAccess) {
> ...
> ```
> 
> Explicitly checking for `true/false` usually implies underlying issues such as - incorrect typing, incomplete typing, or overloading boolean when property is better represented as enum. 
> 
> Also see below comments on checks for explicit `true` 

**2026-04-28** — reviewing a teammate's PR [Freshview/createsend.com#22961](https://git.campmon.com/Freshview/createsend.com/pull/22961#discussion_r165516)
_File: `app/CampMon.Core/Sequences/Models/SequenceConditionType.cs`_

> I had this mapped in  app/CampMon.CmAPI/Endpoints/Sequence/Models/CmSequenceRuleCondition.cs
> 
> Maybe we'll migrate to use yours

**2026-05-21** — reviewing a teammate's PR [Freshview/createsend.com#23242](https://git.campmon.com/Freshview/createsend.com/pull/23242#discussion_r167246)
_File: `srcfrontend/app/campaigns/components/EditSequence/AdvancedSequence/Sidebar/SequenceActivityPanel.tsx`_

> The contract/typing is wrong here. 
> 
> `campaignCompareDetails` can be undefined when the sequence has campaigns but none of them has been sent. (E.g. seq with only a draft root node) 

## Your longest comments — the architectural ones

These are the comments where you went into depth — explaining trade-offs, suggesting design changes, or unpacking a non-obvious issue.

### 2022-09-02 — [Freshview/createsend.com#13570](https://git.campmon.com/Freshview/createsend.com/pull/13570#discussion_r107132) — a teammate's PR
_File: `srcfrontend/app/smscampaigncreationchecklist/components/SmsFromStep/SmsFromStep.tsx` — 1207 chars_

> The type system in Typescript is purely decorative, it only screams and paints red squiggly lines on your editor. 
> Very different from C# where casting actually changes the value underneath or can throw at runtime. 
> Which means what you are doing here won't work. 
> 
> First step is to update `app\cm-api\models\TFNVerificationStatusEnum.ts` (or new name `app\cm-api\models\TollFreeNumberVerificationStatus.ts` ) to match what's getting served from the server - string literals, as seen on the screenshot in your PR description. 
> 
> ```
> export enum TollFreeNumberVerificationStatus {
>     NotApplicable = 'NotApplicable',
>     Unverified = 'Unverified',
>     Pending = 'Pending',
>     Verified = 'Verified',
> }
> ```
> 
> Second step is to update the stuff here. 
> You can't do `<` comparisons with strings so you'll need to do `===` checks. 
> ```
> if (cmSmsClient.tollFreeNumberStatus !== TollFreeNumberVerificationStatus.Verified) {
>   // do stuff
> } else {
>   // do other stuff
> }
> ```
> 
> While you are at it you may want to update `app\cm-api\models\CmSmsClient.ts` interface property `tollFreeNumberStatus` to be of type `TollFreeNumberVerificationStatus` instead of `string` 
> 
> Hope this makes sense. 

---

### 2023-02-01 — [Freshview/createsend.com#14586](https://git.campmon.com/Freshview/createsend.com/pull/14586#discussion_r114254) — a teammate's PR
_File: `app/js/src/app/contacts/copypastesubscribeform/copypastesubscribeform.logic.js` — 702 chars_

> `??` nullish colleasing operator is not available in ie11. 
> https://caniuse.com/mdn-javascript_operators_nullish_coalescing
> 
> `?.` optional chaining operator is also not available in ie11. 
> https://caniuse.com/mdn-javascript_operators_optional_chaining
> 
> 
> I would suggest just dumping the entire code into the online babel transpiler set to ie11.
> https://babeljs.io/repl#?browsers=ie%2011&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=Q&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env&prettier=false&targets=&version=7.20.14&externalPlugins=&assumptions=%7B%7D

---

### 2023-08-10 — [Freshview/createsend.com#15918](https://git.campmon.com/Freshview/createsend.com/pull/15918#discussion_r123927) — a teammate's PR
_File: `srcfrontend/app/commercesettings/pages/ShopifyMigrationStatusAgency/LegacyShopifyIntegrationContextProvider.tsx` — 644 chars_

> Up to you if you want to do a 
> ```
> 
> type MappedIntegrationSuccess = {success: true; isMigrated: boolean; status: ShopifyListsImportStatus; clientId: string};
> type MappedIntegration = MappedIntegrationSuccess | {success: false; clientId: string};
> 
> const isStatusAvailable = (integration: MappedIntegration): integration is MappedIntegrationSuccess =>
>             integration.success && integration.status !== undefined && integration.isMigrated !== undefined;
> 
> const listImportStatusMap = statuses
>                         .filter(isStatusAvailable)
>                         .reduce(... 
> ```
> 
> to avoid the `{status: status!}` below. 

---

### 2026-02-19 — [Freshview/createsend.com#22310](https://git.campmon.com/Freshview/createsend.com/pull/22310#discussion_r160686) — a teammate's PR
_File: `app/CampMon.Data.NetStandard/Crm/CrmLiteRepository.cs` — 572 chars_

> ```suggestion
>                   AND PopulateStatusDateUTC < @StaleThresholdUtc
> ```
> 
> `DateUpdateUTC` is set when the client opts in/out the crm feature and other row modifications, except for the list init population work. 
> 
> `PopulateStatusDateUTC` is set by the sqs consumer when the last batch of work (RawContactDefined events) is submitted to the kafka topic contact pipeline. 
> Hence no more work will be created and the job will eventually become "stale". 
> Rename suggestions welcome we have changed it twice already I still find the name confusing sometimes. 

---

### 2024-10-09 — [Freshview/createsend.com#18249](https://git.campmon.com/Freshview/createsend.com/pull/18249#discussion_r138529) — a teammate's PR
_File: `srcfrontend/app/accountsettings/components/ManageAdministratorsPage/AdministratorRow.tsx` — 548 chars_

> It is missing a line 
> ```
> <div class="js-app" />
> ```
> in https://git.campmon.com/Freshview/createsend.com/blob/8ebde635eb903de0a752c1e7ccb92b799b19f8be/app/Areas/Admin/Views/Account/AccountSettingsOverview.cshtml 
> 
> 
> See for example https://git.campmon.com/Freshview/createsend.com/blob/a4a1327721cb78d3acd850144918e060122a1540/app/Areas/Admin/Views/Account/SmsSettings.cshtml#L19-L20C1
> 
> The cm modal portal relies on that special div to mount the popups. We also use that in some unit tests to verify components are performing as expected. 

---

### 2023-03-16 — [Engineering/workflowbuildercontext.uiservice.core#156](https://git.campmon.com/Engineering/workflowbuildercontext.uiservice.core/pull/156#discussion_r116364) — a teammate's PR
_File: `WorkflowBuilderContext.UIService/ui/components/Report/WorkflowConversionsReportDetails.tsx` — 456 chars_

> Had a chat with a teammate about this - 
> Since `displaySelectedValue` is not dependant on any asynchronous changes within this component, thus don't need its own state setter, we can replace 
> ```
> const [displaySelectedValue, setDisplaySelectedValue] = useState(initValue);
> ```
> with 
> ```
> const displaySelectedValue = isReportingError ? (lastSuccessfulFromDateUtc ?? initValue) : selectedValue;
> ```
> and avoid the whole useEffect event loop problem. 

---

### 2025-07-03 — [Engineering/contentbuildercontext.staticresourceservice.core#1096](https://git.campmon.com/Engineering/contentbuildercontext.staticresourceservice.core/pull/1096#discussion_r146668) — a teammate's PR
_File: `ContentBuilderContext.StaticResourceService/static_src/ts/modules/emailbuilder/content-blocks/ckeditor-text-color.plugin.ts` — 429 chars_

> This looks scary. 
> Reading this as isolated code, it reads like it can run into array access out of bounds or null reference errors. (Which might not happen in practice)
> 
> https://ckeditor.com/docs/ckeditor4/latest/api/CKEDITOR_dom_element.html#method-getNext
> 
> I don't like iterating on `i` and especially when it's not used. Maybe consider using iterator loop pattern and `CKEDITOR.dom.element.prototype.hasNext()` instead. 

---

### 2026-01-30 — [Freshview/createsend.com#22070](https://git.campmon.com/Freshview/createsend.com/pull/22070#discussion_r159369) — a teammate's PR
_File: `app/CampMon.CmAPI/Endpoints/CrmLite/Models/CmCrmCustomerDetails.cs` — 390 chars_

> ```
> Action GetCrmCustomerDetails on controller CrmLiteController includes a DateTime property in the response type System.Threading.Tasks.Task`1[Microsoft.AspNetCore.Mvc.ActionResult~1[CampMon.CmAPI.Endpoints.CrmLite.Models.CmCrmCustomerDetails]] 
> 
> ```
> 
> Should be returning `string` in cmapi models. 
> You can probably just `.ToString("o")` the DateTime value. (Check with csharp crew)

---

### 2023-03-01 — [Freshview/createsend.com#14788](https://git.campmon.com/Freshview/createsend.com/pull/14788#discussion_r115719) — a teammate's PR
_File: `app/Pronto.SubscriberPreferences/Views/Shared/Default.Master` — 380 chars_

> Can you assign the `$('#mobile')` queries to a local variable please, and try to only do the queries once per dom element. 
> 
> `jQuery()` selector calls can get very expensive and slow (especially in older browsers). 
> 
> This [particular case is probably fine](https://learn.jquery.com/performance/optimize-selectors/) but it's better to minimise the selector queries in general. 

---

### 2026-04-21 — [Freshview/createsend.com#22903](https://git.campmon.com/Freshview/createsend.com/pull/22903#discussion_r164942) — a teammate's PR
_File: `srcfrontend/app/audience/components/CrmLite/CrmLiteApi.ts` — 374 chars_

> Do you need to explicitly check for `false` here? 
> If not it's better written as 
> ```
> if (!result.hasCrmAccess) {
> ...
> ```
> 
> Explicitly checking for `true/false` usually implies underlying issues such as - incorrect typing, incomplete typing, or overloading boolean when property is better represented as enum. 
> 
> Also see below comments on checks for explicit `true` 

---
