Answers Student Teams could potentially get - bonus points if they discover ones not listed

Functional - these are broken into requirements that support particular use cases

**E-mailer sends e-mails
Must be able to generate 3 different types of e-mails
Must be possible to schedule when e-mails are sent
Must detect preferred language of subscriber and send e-mail in that language.
Must be integrated with MySQL, Exim, the ad copy and links to content.

**User creates e-mail content(This is the toughest requirement because none of the stakeholders realize they need it)
User must be able to create advertising copy/boilerplate for an e-mail based on send date/language/topic combo.

**Web page content selector/generator
Must be possible to schedule when web pages are generated.
Must be possible to create pages for a topic-language combo.
Desirable that system automatically execute article query based on language-topic combo.
Must be possible to select multiple articles from list/query.
Must be possible to layout page using WYSIWYG.
Desirable that it be integrated with Django CMS.
Desirable that it send an e-mail reminder to generate page.
Desirable that an integrated machine translator be used for gisting page content.

**Outside vendor lead integrator
Script?  GUI?  Possibilities are wide open.

Non functional

Interoperability - Backend processing portion must be compatible with LAMP setup and other existing applications.  Front end applications must work on a Windows 7 machine.
Security - subscriber, registered user and lead PII must be protected IAW country regs.
Scalability - system must be able to send in excess of 1 million e-mails in an evening while not taxing other running processes
Capacity - system must be able to handle increased load of at least 20% to meet CEO's optimistic goals.
Supportability - IT staff must be able to maintain the system.


What issues need to be resolved?

How is e-mail content captured?
How are third-party leads integrated into the system?
How are the moving parts coordinated?
Marketing and science editor have different ideas about web page content generation.
IT uninformed about outside vendor data.

