# Registration Landscape White Paper

This paper aims to provide a systematic overview of the key stakeholders, considerations, concerns around building of a registry for remotely piloted aircrafts (RPAS) or unmanned aircrafts (UA). Upcoming regulations the EU mandate that every National Authority in a Member state maintain a registry that holds the details of the operators and potentially their equipment, certifications and other data. This is a complex task for the National Aviation Authority (NAA), so this document provides considerations that must be addressed when building a registry. To illustrate the complexity of this space, the simple question of what is the best way for the user to register opens up a number of open issues that are actively being discussed: should the user register with the RPAS / UA manufacturer, the retailer or the Unmanned Traffic Management provider?  This paper does not cover the specific technical implementation: that is left for the individual NAAs to address with their IT providers, however, it provides some of the key requirements that they should be considering when working with their solution providers. This document is deliberately generic and aims to cover key components for the registry as it develops in this dynamic environment. This initial work is aimed to be compatible with any requirements / programs from other international organizations such as ICAO that may arise in the future. It is flexible enough that a registry implementation derived from this document should accommodate any additional data / requirements that arise out of the dynamic landscape in the future.

## Scope of Document

Building IT systems working with third party contractors is a large and complicated problem. In a space as complicated as U-Space / UTM there is a urgent need to identify stakeholders, develop a scope of the project. This document is aimed to provide a general overview of the registration landscape and help CAAs and National Authorities effectively engage with their IT staff and solution providers to build a registry. Some CAAs will opt for competitive tenders from outside and IT solution provides will be working with the CAAs. This document it is aimed to help define the scope of the project to ensure that the work is future proof. We do this identifying the technical considerations, actors in the respective member states and also data and entities that they should consulting to build a registry that is compatible with U-Space and UTM. There is considerable challenge with this given the dynamic nature of the market and regulation and this document serves as a base for any project specification / plan for the CAAs. The document stays away from recommending specific technologies, identification / authentication systems since it is expected that every CAA would have to work with their local / national ID system that may or may not exist.

## Background

In a multi-state, multi-actor environment that the U-Space in EU operates in, there are numerous considerations beyond the specific registration data that need to be addressed. This is relevant to other jurisdictions as well: especially in non-EU countries and countries and working with a combined EU + non-EU registration environment for e.g. Switzerland.

The trend in drone regulations is such that Governments across the world would mandate that RPAS / UA operators and potentially the equipment should be registered. We should divergence on the specific criteria such as weight thresholds etc. but broadly we should expect agreement on the spirit and intent of the registration and maintaining records. In addition, we should expect certain class of operations in certain class of airspace may not require any permissions or registration data while flight permissions, registration data would be required for others.

As the operations become more complex, it should also be expected that there would be a training / certification component to the registry like a driver&#39;s license. The operator may need to be trained and may need to maintain their certifications for their staff and company. All this information will be required to be stored and queried digitally and some information may be made available to some queries depending on who / what the purpose is. To begin with, we review the EU regulation, since it is serves as a good model of what to expect for the future where many countries must implement independent registries. This is in contrast with the US / FAA model where the FAA serves as the central point of registration and control. It is unclear how the FAA will share / query the information with its neighbors e.g. Canada, Mexico. The upcoming EU legislation mandates the following about registration:

- UAS operator of an UAS of more than 250 gr to be registered in the national register where it has its principal place of business. Additionally, it should be registered if it poses a security, privacy or environmental risk
- The national register shall be interoperable.
- The system needs to be capable of dealing with hundreds of thousands of operators, must be easily accessible (mainly electronically).
- Basic functions to assure integrity and an up-to date information should be implemented.
- Privacy needs to be ensured, however access to the data across Europe for authorized enforcement bodies needs to be available.

![EASA Drone Classifications](https://i.imgur.com/MQYb0hJ.png)

The EU regulation specifies that the registration of UAS is a national responsibility and each Member State and the state may designate a competent authority for that purpose. There is a requirement that this registry is accessible in real-time which means that there are some requirements about technology and availability and support operations from an IT support and operations point of view. The following table details the requirements for U-Space from an EU point of view. (Source: EASA Opinion 01-2018)

## Registry usage and entry point

The primary use of a registry is to store information and data about UAS operators, their licenses, training and check for expiration of data and share and query information. It should be anticipated that the registry will have many unintended uses as well. For e.g. there is a requirement to have a Fire-resistant placard for displaying registration information on the UAS. This registration number would have to be cross linked to the registry so transmission of this information to placard manufacturer is necessary. The registry could be used by law enforcement to make queries, issue warnings from time to time etc.

The question of where and when does an operator register is an open one. This is a important question because it has implications on compliance, the ease of use for the operator and also ensure that the registry includes all operators and drones sold in the jurisdiction. The following is a list of scenarios that could be implemented to ensure all operators are compliant with the regulations:

| How and when does a operator register? | Pros | Open questions |
| --- | --- | --- | -- |
| CAA asks all operators to go to their website to register and a get an operator ID. | The registration website is the single point of entry for operators to enter their information. | 1. How to ensure that all operators will indeed register  <br>2. If the drones are also being registered, how to ensure that all drones are in the registry and track resale / air-worthiness conditions. <br>3. In some jurisdictions, the &quot;operatorid&quot; might be required to be pasted on the drone, how does one ensure that it is?|
| Implement registry entry at Point of Sale. In this scenario, the retailer enters the information at point of sale so that owners are linked to equipment they purchase. | This method ensures that registration data is captured at the source and has the potential to ensure compliance. | 1. How do you track transfers? <br> 2. How to ensure compliance from the retailers? <br> 3. How to manage returns / repairs? 4. How do manage Internet based sales / delivery? |
| The CAA asks UTM providers / hardware manufacturers to share information about registration. | Once a RPAS / UA is purchased, the operator must register with the hardware manufacturer or the UTM service provider. This data could potentially be shared with the CAA to ensure that all operators (and potentially equipment) is registered. |1. How to keep track of the data sharing and transfer? <br> 2. UTM providers and hard ware manufacturers are private entity in a dynamic market, how to ensure that all current future ones will be part of this program? |

All the strategies above are valid entry points to the registry and a decision must be made by the CAA to pick one or more methods from the list above.

## Interested parties

The following is a list of interested parties that would be interested in using / querying a registry. The goal of this list to identify potential parties who might be interested in the registry. It may be that some of the parties listed below use other party to query or lookup the registry, so in that these the list is interconnected. For e.g. a Cultural Heritage agency might use the ANSP to query the registry. We are not saying that everyone should have a direct access to the registry, which is one option, but the aim is to list out all the cases where a registry might be queried electronically. We are also not saying that all information required by these entities should be in the registry, but this should give a good idea of what the interested parties would be looking for and their motivations. This should guide some of the access and authentication considerations. One way to look at this list is to identify immediate entities that you would like to provide access to in the first release of the registry, gradually increasing scope and access as you move forward.

| Entity Name | Entity Type | Notes |
| --- | --- | --- |
| National Aviation Authority | National Agency | Per the EU regulation, the Member state must nominate a competent authority to build, maintain and operate a registry. We anticipate that in most cases it would be the Civil Aviation Authority |
| USS operators | Private Company | A company that provides software / Apps for drone flights might need to query the registry to get information. Some apps have capability to submit flight plans.   |
| Air Navigation Service Provider | Private Company / Public Private Entity | An ANSP is in charge of managing controlled air-space, they will need to query and look at the registry to integrate that into their existing software / systems. |
| Law Enforcement (National / Local / International Police) | Public Entity | Law Enforcement might need to look at a registry to check the name address and other details of the operators. In many cases it can be expected that the law enforcement maintains their own databases and might need privileged access to the data in real time. |
| Local public administration (e.g. Canton, local government) | Public Entity | In many cases a member state may have administrative boundaries e.g. local governments, state governments that might need to query the national registry to check registration details. They may have specific requirements, laws that prohibit certain types of flights at a time and any operator breaking the rules might need to be queried, fined seamlessly.   |
| Cultural / Heritage Agencies | Public Entity | In some cases, drone flights over national / world heritage sites might be restricted. An agency that manages the cultural sites would be interested in querying the registry for operator / equipment details.   |
| Environmental Agencies | Public Entity | Some environmental agencies might be interested in checking the operator registration details before approving / rejecting flights in their jurisdiction or in the event of a natural disaster: floods etc. |
| Air sports / Gliders / Balloons | Association | The FAI is an association that manages events and pilots for gliders, balloons etc. in a case where there is an event they might need to check if the drones there are registered, licensed and insured. |
| Anti-Drone companies / Private Security services | Private Companies | There are companies that specialize in taking down unauthorized drones or drones that invade private airspace. In some cases, a criminal / civil complaint may be necessary. In such a case they may need to check the registration data. |
| Organizations managing a specific area (e.g. ports, buildings) | Private Company / Public Private Entity | Drone flights over certain areas need specific clearance / approvals and the authority managing those might need to verify / check the identity, training and other requirements from the registry |
| Insurance Companies / Accident investigators | Private Company | As drone flights become common, insurance companies might need to check if the operator has training, license and other information that is up-to-date. |
| Cross border agencies | Public Agency | In some cases, drones would fly across international borders and authorities from the neighboring jurisdiction might need to look at registration data |
| ICAO | International Organization | ICAO has an interest in Drones and specifically a cross-border drone registration. They might require a unique ICAO number like for aircraft, in which case they would query the national database for registration information. |
| Private Citizens | Citizens | In some cases, citizens might need to query registration data if they see a drone on their land to return it to the operator, make a complaint etc. |
| Revenue Authorities | Public Authorities | In cases where there is a special registration / equipment that may be taxed Revenue authorities might need to check if the appropriate tax is paid for that air. E.g. some cars have a special tax associated with them that has to be paid every year. |
| EASA / ANSP | Public Authorities | In some cases, to check the certificate of air worthiness needs to be checked and a registry could be a good place to store it. |
| Military | Public Authorities | When drones fly too close to military bases or are unauthorized, it might require further action from the military including civil complaints. |
| Insurance Companies | Private Company | As drones get more popular, insurance might become mandatory, the companies might need to communicate with the registry to provide their insurance number. In addition, the registry would be interesting for insurance companies as a marketing opportunity to identify operators who existing insurance is expiring |
| Marketing Companies | Private Company | For e.g. a drone training company might want to look at the registry to see all operators whose license is expiring or need a new training to market their raining to the operators. |
| Drone Equipment Retailers | Private Company | Both of these could be mandated / interested in submitting registration information and also might be interested in querying which operators have access to their particular RPAS / UAS |
| Drone Manufacturers | Private Company |

## Registry Identification / Authentication

It should be expected that there would be many ways to identify and authenticate on the registry. Several countries have national ID system in other there is a colloquial way to identify e.g. VAT number of operator or Social Security numbers, bank account numbers, postal ID etc. These are not specifically meant as identification but are used anyway. A good assessment of identification and the data / documents required could be the data required to open a bank account in the country. This serves as a good set of documents that could be required for a registry both in terms of security and documents required. It should be anticipated that the registry will have to deal with existing identification system in the country, so we would recommend interacting with them at the start. In addition given the interested parties above and the cross-boundary nature of those, provision should be made to accommodate entities that may not possess a national / regional ID to be able to query the registry. Not everyone would be entitled to a national ID so appropriate provisions must be made to the database to accommodate requests for them both electronically and otherwise.

In some cases, the CAA might issue licenses, badges based on the registration data e.g. in Dubai. In that case additional data such as a photograph and motor vehicle license type card might need to be linked to the registry. Also in Dubai, a standardized  QR-code is issued and the QR code contains information the drone based upon its owner, type, commission date and unique identifier.

## Registry Data

This section details the information that could be held in the registry and updated, in some sense it is a working list that we think would need to be stored in the registry given the different actors. It is assumed that while the CAA builds and maintains the registry the requirements for the registry will come from different entities outside of the jurisdiction / organization of the CAA and potentially the need to interact, extract data from existing databases or at least have a way to communicate with them.

It is acknowledged that not all data requirements would be apparent immediately, so it is recommended that the operators consider a renewal mechanism, so everyone registered update their data at a certain period of time to recertify so that all entities in the registry are compliant at all time and the ones that are could have their registration revoked.

| Data | Type | Details |
| --- | --- | --- |
| Operator Name | Text | Name of the operator |
| Operator Address | Text | Operating address of the operator |
| Operator ID | Unique number | An ID assigned by the registry for that operator |
| Operator Type | Text | What type of operator is this? Private, Public, Special |
| Operator Authorization type | Text | What type of operations this operator is approved for? E.g. C0, C1, C2 etc. |
| Insurance number | Text | Details about the insurance |
| Training Certifications | Text | Training details |
| Operator contact, email | Text | Email and phone number of the operator |
| Equipment type | Text | Type of equipment registered |
| Equipment COA | Text | Any certifications of airworthiness about the equipment |
| License expiration date | Date | Date till which the details are valid |
|   |   |   |

### Data requirements

One of the goals of the registry is to ensure that the data is not &quot;stale&quot; so it is recommended that the entities in the registry update / recertify themselves every X number of years, that could be every one year or three years or whatever the State decides. This means that the onus of registration and keeping up with the requirements is with the operator and it also gives the CAA / registry operator to accommodate changes to the registration as the market develops and new actors come in. Additionally, processes should be setup to conduct regular audits to ensure that there is a integrity check and backups to ensure smooth running of the registry.  As an example, a system where the registry entries automatically expire after one or two years and the operator is sent reminders 30, 15 and 7 days before expiry and a final warning after expiration that the registration has expired and a operating a RPAS / UA without registration may invoke penalties and fines sent via email / SMS could be implemented.

### Reading from Registry

Given the number of interested parties, there would be a set of information that would be provided by default depending on the privacy laws of the country. However, reading from the registry should be enabled non-trivially for certain classes of interested parties. For others, there might be a need to provide special access or agreements that need to be managed and maintained locally at a member state level.

### Writing to Registry

In some cases, especially when the registry is large and complex with different actors, there might be a need to automate certain writing of data in the registry (e.g. insurance information). This information is received by third parties and then entered in the registry. Therefore, appropriate write privileges / roles should be built in the registry to ensure smooth operations. Regular audits and procedures to update databases must be established to ensure data consistency and error free dataset.

### Information Transfer

It should be assumed that data in the registry will cross borders and therefor appropriate provisions for international data transfer in accordance to local privacy regulations / agreements should be made. For e.g. Russia may enter an agreement with Finland to share drone registration data. In that case data from a non-EU member to an EU member would be shared appropriately.

In the same way, data will flow between different entities within a jurisdiction: insurance companies, local police etc. The registry should facilitate such data transfers, electronically while ensuring security and privacy.

## Governance Structures

Viewing this database holistically as a way to manage RPAS / UAS governance is a crucial first step in this process. Therefore, it is instructive to not consider the registry as simply another IT project within the CAA. From this point of view, RPAS/UAS governance encompasses their design, testing, certification, manufacture, retail, pilot training, operational regulatory compliance, maintenance, transfer of ownership and final de-commissioning.  All these processes would entail the use of a registry and could provide a rich source of data (anonymized as required by local and international data privacy laws) to help enhance safety and interoperability.  The true measure of any such registry would lie in its ability to enhance RPAS/UA usage while at the same time contributing to their safe, reliable and value addition operation.

The registry operator must consider the governance structures in the local environment to ensure that they are compatible with it. For e.g. in a Federal structure like Switzerland the governing authority is at a Cantonal level. In this case, the canton&#39;s IT systems stakeholders should be engaged in the development of the database so that they have access to it and the need for them to duplicate the tools is minimized. It could be assumed that these local entities might need a copy of the database for local use.

From an administration point of view, a way for them to communicate changes that should be established. The registry is a living document and appropriate process for changes, updates and requests with the different members should be ensured. In addition, it should be expected that the maintainers liase with other entities nationally and internationally to share best practices and incorporate their process. This could include weekly, monthly quarterly meetings and ways to address changes and grievances. The maintenance of the registry is a critical function of the IT organization so appropriate organizational structures must be put in place to ensure that the stakeholders are satisfied.

The aim is not mandate a large bureaucratic structure to manage the registry but to ensure that the authorities have not overlooked this important function. Building the registry is just half the story, ongoing maintenance, upgrades and management in the local context is the more important critical function of this exercise.

## Acknowledgements

We are thankful to Mr. Michael Rudolph ([michael.rudolph@dcaa.gov.ae](mailto:michael.rudolph@dcaa.gov.ae)) , Head of Airspace Safety Section in the Aviation and Airports Safety Department of the Dubai Civil Aviation Authority for comments and review.

## Revision History

| Version | Date | Author | Change comments |
| --- | --- | --- | --- |
| 0.3 | 28-June-2018 | Dr. Hrishikesh Ballal | Added section about registry entry, incorporated comments from external reviewss |
| 0.2 | 21-June-2018 | Dr. Hrishikesh Ballal | Restructured sections, added information about authentication, changed text |
| 0.1 | 19-June-2018 | Dr. Hrishikesh Ballal | Initial creation |