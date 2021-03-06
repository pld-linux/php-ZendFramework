#
# Conditional build:
%bcond_with	tests		# build with tests

# NOTE:
# - ZendXml has it's own versioning schema, version 1.0.1 as of 2.4.8 ZF2 release
# - ZF2 installs to /usr/share/php/Zend, while ZF1 installs to /usr/share/pear/Zend

Summary:	Zend Framework 2
Name:		php-ZendFramework
Version:	2.4.13
Release:	2
License:	BSD
Group:		Development/Languages/PHP
Source0:	https://packages.zendframework.com/releases/ZendFramework-%{version}/ZendFramework-%{version}.tgz
# Source0-md5:	a61dd64158d1f3edea1290959c3fd783
# git clone https://github.com/zendframework/zf2.git
# cd zf2; git checkout release-2.4.8
# tar czf ../ZendFramework-tests-2.4.8.tgz tests
#Source1:	ZendFramework-tests-%{version}.tgz
Source2:	autoload.php
Patch0:		zf-mail-2.4-fixes.patch
URL:		https://framework.zend.com/
%if %{with tests}
BuildRequires:	phpunit >= 4.0.0
%endif
Requires:	php(core) >= 5.3.23
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zend Framework 2 is an open source framework for developing web
applications and services using PHP 5.3+. Zend Framework 2 uses 100%
object-oriented code and utilizes most of the new features of PHP 5.3,
namely namespaces, late static binding, lambda functions and closures.

Zend Framework 2 evolved from Zend Framework 1, a successful PHP
framework with over 15 million downloads.

%package Authentication
Summary:	Zend Framework 2: Authentication Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.authentication.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Crypt = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-Ldap = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	%{name}-Uri = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(date)
Suggests:	php(hash)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Authentication
The Zend\Authentication component provides an API for authentication
and includes concrete authentication adapters for common use case
scenarios.

Zend\Authentication is concerned only with authentication and not with
authorization. Authentication is loosely defined as determining
whether an entity actually is what it purports to be (i.e.,
identification), based on some set of credentials. Authorization, the
process of deciding whether to allow an entity access to, or to
perform operations upon, other entities is outside the scope of
Zend\Authentication. For more information about authorization and
access control with Zend Framework, please see the
Zend\Permissions\Acl or Zend\Permissions\Rbac component.

%package Barcode
Summary:	Zend Framework 2: Barcode Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.barcode.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(dom)
Suggests:	php(gd)
Suggests:	php(iconv)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Barcode
Zend\Barcode\Barcode provides a generic way to generate barcodes. The
Zend\Barcode component is divided into two subcomponents: barcode
objects and renderers. Objects allow you to create barcodes
independently of the renderer. Renderer allow you to draw barcodes
based on the support required.

%package Cache
Summary:	Zend Framework 2: Cache Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-cache
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Serializer = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Cache
%{summary}

Optional:
- APC (php-pecl-apc)
- DBA (php-dba)
- Memcache (php-pecl-memcache)
- Memcached (php-pecl-memcached)
- Mongo (php-pecl-mongo)
- Redis (php-pecl-redis)
- XCache (php-xcache)

%package Captcha
Summary:	Zend Framework 2: CAPTCHA Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.captcha.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Math = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	%{name}-Text = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(gd)
Suggests:	php(spl)

%description Captcha
CAPTCHA stands for "Completely Automated Public Turing test to tell
Computers and Humans Apart'; it is used as a challenge-response to
ensure that the individual submitting information is a human and not
an automated process. Typically, a CAPTCHA is used with form
submissions where authenticated users are not necessary, but you want
to prevent spam submissions.

CAPTCHAs can take a variety of forms, including asking logic
questions, presenting skewed fonts, and presenting multiple images and
asking how they relate. The Zend\Captcha component aims to provide a
variety of back ends that may be utilized either standalone or in
conjunction with the Zend\Form component.

%package Code
Summary:	Zend Framework 2: Code Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Suggests:	%{name}-Stdlib = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)
Suggests:	php(tokenizer)

%description Code
Provides facilities to generate arbitrary code using an object
oriented interface.

%package Config
Summary:	Zend Framework 2: Config Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.config.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(xml)
Suggests:	php(xmlreader)
Suggests:	php(xmlwriter)

%description Config
Zend\Config is designed to simplify access to configuration data
within applications. It provides a nested object property-based user
interface for accessing this configuration data within application
code. The configuration data may come from a variety of media
supporting hierarchical data storage. Currently, Zend\Config provides
adapters that read and write configuration data stored in .ini, JSON,
YAML and XML files.

%package Console
Summary:	Zend Framework 2: Console Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.console.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Filter = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)
Suggests:	php(xml)

%description Console
Zend Framework 2 features built-in console support.

When a Zend\Application is run from a console window (a shell window),
it will recognize this fact and prepare Zend\Mvc components to handle
the request. Console support is enabled by default, but to function
properly it requires at least one console route and one action
controller to handle the request.

- Console routing allows you to invoke controllers and action
  depending on command line parameters provided by the user.
- Module Manager integration allows ZF2 applications and modules to
  display help and usage information, in case the command line has not
  been understood (no route matched).
- Console-aware action controllers will receive a console request
  containing all named parameters and flags. They are able to send
  output back to the console window.
- Console adapters provide a level of abstraction for interacting with
  console on different operating systems.
- Console prompts can be used to interact with the user by asking him
  questions and retrieving input.

%package Crypt
Summary:	Zend Framework 2: Crypt Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.crypt.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Math = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	php(hash)
Suggests:	php(mcrypt)
Suggests:	php(openssl)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Crypt
Zend\Crypt provides support of some cryptographic tools. The available
features are:

- encrypt-then-authenticate using symmetric ciphers (the
  authentication step is provided using HMAC)
- encrypt/decrypt using symmetric and public key algorithm (e.g. RSA
  algorithm)
- generate digital sign using public key algorithm (e.g. RSA
  algorithm)
- key exchange using the Diffie-Hellman method
- Key derivation function (e.g. using PBKDF2 algorithm)
- Secure password hash (e.g. using Bcrypt algorithm)
- generate Hash values
- generate HMAC values

The main scope of this component is to offer an easy and secure way to
protect and authenticate sensitive data in PHP. Because the use of
cryptography is not so easy we recommend to use the Zend\Crypt
component only if you have a minimum background on this topic.

%package Db
Summary:	Zend Framework 2: DB Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-db
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-EventManager = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(pcre)
Suggests:	php(pdo)
Suggests:	php(spl)

%description Db
%{summary}

Optional:
- ibm_db2 (http://pecl.php.net/package/ibm_db2)
- mysqli (php-mysql)
- oci8 (http://pecl.php.net/package/oci8)
- pgsql (php-pgsql)
- sqlsrv (http://pecl.php.net/package/sqlsrv)

%package Debug
Summary:	Zend Framework 2: Debug Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-Escaper = %{version}-%{release}
Suggests:	php(pcre)

%description Debug
%{summary}

Optional: XDebug (php-pecl-xdebug)

%package Di
Summary:	Zend Framework 2: DI Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.di.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Code = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Di
Dependency Injection (here-in called DI) is a concept that has been
talked about in numerous places over the web. Simply put, we'll
explain the act of injecting dependencies simply with this below code:

$b = new MovieLister(new MovieFinder());

Above, MovieFinder is a dependency of MovieLister, and MovieFinder was
injected into MovieLister.

%package Dom
Summary:	Zend Framework 2: DOM Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.dom.intro.html
Requires:	%{name} = %{version}-%{release}
Suggests:	php(dom)
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(xml)

%description Dom
The Zend\Dom component provides tools for working with DOM documents
and structures. Currently, we offer Zend\Dom\Query, which provides a
unified interface for querying DOM documents utilizing both XPath and
CSS selectors.

%package Escaper
Summary:	Zend Framework 2: Escaper Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.escaper.introduction.html
Requires:	%{name} = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(iconv)
Suggests:	php(mbstring)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Escaper
The OWASP Top 10 web security risks study lists Cross-Site Scripting
(XSS) in second place. PHP's sole functionality against XSS is limited
to two functions of which one is commonly misapplied. Thus, the
Zend\Escaper component was written. It offers developers a way to
escape output and defend from XSS and related vulnerabilities by
introducing contextual escaping based on peer-reviewed rules.

%package EventManager
Summary:	Zend Framework 2: EventManager Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.event-manager.event-manager.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	php(spl)

%description EventManager
The EventManager is a component designed for the following use cases:

- Implementing simple subject/observer patterns.
- Implementing Aspect-Oriented designs.
- Implementing event-driven architectures.

The basic architecture allows you to attach and detach listeners to
named events, both on a per-instance basis as well as via shared
collections; trigger events; and interrupt execution of listeners.

%package Feed
Summary:	Zend Framework 2: Feed Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.feed.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Escaper = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(date)
Suggests:	php(dom)
Suggests:	php(hash)
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(tidy)
Suggests:	php(xml)

%description Feed
Zend\Feed provides functionality for consuming RSS and Atom feeds. It
provides a natural syntax for accessing elements of feeds, feed
attributes, and entry attributes. Zend\Feed also has extensive support
for modifying feed and entry structure with the same natural syntax,
and turning the result back into XML. In the future, this modification
support could provide support for the Atom Publishing Protocol.

Zend\Feed consists of Zend\Feed\Reader for reading RSS and Atom feeds,
Zend\Feed\Writer for writing RSS and Atom feeds, and
Zend\Feed\PubSubHubbub for working with Hub servers. Furthermore, both
Zend\Feed\Reader and Zend\Feed\Writer support extensions which allows
for working with additional data in feeds, not covered in the core API
but used in conjunction with RSS and Atom feeds.

%package File
Summary:	Zend Framework 2: File Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-file
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(fileinfo)
Suggests:	php(hash)
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(tokenizer)

%description File
%{summary}

%package Filter
Summary:	Zend Framework 2: Filter Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.filter.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Crypt = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-Servicemanager = %{version}-%{release}
Suggests:	%{name}-Uri = %{version}-%{release}
Suggests:	php(bz2)
Suggests:	php(date)
Suggests:	php(iconv)
Suggests:	php(lzf)
Suggests:	php(mbstring)
Suggests:	php(openssl)
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(zip)
Suggests:	php(zlib)

%description Filter
The Zend\Filter component provides a set of commonly needed data
filters. It also provides a simple filter chaining mechanism by which
multiple filters may be applied to a single datum in a user-defined
order.

%package Form
Summary:	Zend Framework 2: Form Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.form.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-InputFilter = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Captcha = %{version}-%{release}
Suggests:	%{name}-Code = %{version}-%{release}
Suggests:	%{name}-EventManager = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-View = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(intl)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Form
Zend\Form is intended primarily as a bridge between your domain models
and the View Layer. It composes a thin layer of objects representing
form elements, an InputFilter, and a small number of methods for
binding data to and from the form and attached objects.

The Zend\Form component consists of the following objects:

- Elements, which simply consist of a name and attributes.
- Fieldsets, which extend from Elements, but allow composing other
  fieldsets and elements.
- Forms, which extend from Fieldsets (and thus Elements). They provide
  data and object binding, and compose InputFilters. Data binding is
  done via ZendStdlibHydrator.

%package Http
Summary:	Zend Framework 2: HTTP Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.http.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Loader = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Uri = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(curl)
Suggests:	php(date)
Suggests:	php(fileinfo)
Suggests:	php(openssl)
Suggests:	php(pcre)
Suggests:	php(spl)
Suggests:	php(zlib)

%description Http
Zend\Http is a primary foundational component of Zend Framework. Since
much of what PHP does is web-based, specifically HTTP, it makes sense
to have a performant, extensible, concise and consistent API to do all
things HTTP. In nutshell, there are several parts of Zend\Http:

- Context-less Request and Response classes that expose a fluent API
  for introspecting several aspects of HTTP messages:
  - ** Request line information and response status information
  - ** Parameters, such as those found in POST and GET
  - ** Message Body
  - ** Headers
- A Client implementation with various adapters that allow for sending
  requests and introspecting responses.

%package I18n
Summary:	Zend Framework 2: i18n Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.i18n.translating.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	php(intl)
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	%{name}-Config = %{version}-%{release}
Suggests:	%{name}-EventManager = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-View = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(date)
Suggests:	php(pcre)
Suggests:	php(spl)

%description I18n
ZendI18n comes with a complete translation suite which supports all
major formats and includes popular features like plural translations
and text domains. The Translator component is mostly dependency free,
except for the fallback to a default locale, where it relies on the
Intl PHP extension.

The translator itself is initialized without any parameters, as any
configuration to it is optional. A translator without any translations
will actually do nothing but just return the given message IDs.

%package InputFilter
Summary:	Zend Framework 2: InputFilter Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.input-filter.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Filter = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(spl)

%description InputFilter
The Zend\InputFilter component can be used to filter and validate
generic sets of input data. For instance, you could use it to filter
$_GET or $_POST values, CLI arguments, etc.

%package Json
Summary:	Zend Framework 2: JSON Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.json.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-Server = %{version}-%{release}
Suggests:	%{name}-Zendxml = %{version}-%{release}
Suggests:	php(json)
Suggests:	php(mbstring)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Json
Zend\Json provides convenience methods for serializing native PHP to
JSON and decoding JSON to native PHP.

JSON, JavaScript Object Notation, can be used for data interchange
between JavaScript and other languages. Since JSON can be directly
evaluated by JavaScript, it is a more efficient and lightweight format
than XML for exchanging data with JavaScript clients.

In addition, Zend\Json provides a useful way to convert any arbitrary
XML formatted string into a JSON formatted string. This built-in
feature will enable PHP developers to transform the enterprise data
encoded in XML format into JSON format before sending it to
browser-based Ajax client applications. It provides an easy way to do
dynamic data conversion on the server-side code thereby avoiding
unnecessary XML parsing in the browser-side applications. It offers a
nice utility function that results in easier application-specific data
processing techniques.

%package Ldap
Summary:	Zend Framework 2: LDAP Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.ldap.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	php(ldap)
Suggests:	%{name}-EventManager = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(iconv)
Suggests:	php(json)
Suggests:	php(mbstring)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Ldap
Zend\Ldap\Ldap is a class for performing LDAP operations including but
not limited to binding, searching and modifying entries in an LDAP
directory.

%package Loader
Summary:	Zend Framework 2: Loader Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-loader
Requires:	%{name} = %{version}-%{release}
Suggests:	php(bz2)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Loader
%{summary}

%package Log
Summary:	Zend Framework 2: Log Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.log.overview.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Console = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Escaper = %{version}-%{release}
Suggests:	%{name}-Mail = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(dom)
Suggests:	php(json)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Log
Zend\Log\Logger is a component for general purpose logging. It
supports multiple log backends, formatting messages sent to the log,
and filtering messages from being logged. These functions are divided
into the following objects:

- A Logger (instance of Zend\Log\Logger) is the object that your
  application uses the most. You can have as many Logger objects as you
  like; they do not interact. A Logger object must contain at least one
  Writer, and can optionally contain one or more Filters.
- A Writer (inherits from Zend\Log\Writer\AbstractWriter) is
  responsible for saving data to storage.
- A Filter (implements Zend\Log\Filter\FilterInterface) blocks log
  data from being saved. A filter is applied to an individual writer.
  Filters can be chained.
- A Formatter (implements Zend\Log\Formatter\FormatterInterface) can
  format the log data before it is written by a Writer. Each Writer has
  exactly one Formatter.

Optional: MongoDB (php-pecl-mongo)

%package Mail
Summary:	Zend Framework 2: Mail Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.mail.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Crypt = %{version}-%{release}
Requires:	%{name}-Loader = %{version}-%{release}
Requires:	%{name}-Mime = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(date)
Suggests:	php(iconv)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Mail
Zend\Mail provides generalized functionality to compose and send both
text and MIME-compliant multipart email messages. Mail can be sent
with Zend\Mail via the Mail\Transport\Sendmail, Mail\Transport\Smtp or
the Mail\Transport\File transport. Of course, you can also implement
your own transport by implementing the
Mail\Transport\TransportInterface.

%package Math
Summary:	Zend Framework 2: Math Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.math.introduction.html
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(bcmath)
Suggests:	php(mcrypt)
Suggests:	php(openssl)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Math
Zend\Math namespace provides general mathematical functions. So far
the supported functionalities are:

- Zend\Math\Rand: A random number generator
- Zend\Math\BigInteger: A library to manage big integers

Optional: php-gmp

%package Memory
Summary:	Zend Framework 2: Memory Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	php(spl)

%description Memory
%{summary}

%package Mime
Summary:	Zend Framework 2: MIME Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.mime.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Mail = %{version}-%{release}
Suggests:	php(iconv)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Mime
Zend\Mime\Mime is a support class for handling multipart MIME
messages. It is used by Zend\Mail and Zend\Mime\Message and may be
used by applications requiring MIME support.

Optional: %{name}-Mail

%package ModuleManager
Summary:	Zend Framework 2: ModuleManager Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.module-manager.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Config = %{version}-%{release}
Suggests:	%{name}-Console = %{version}-%{release}
Suggests:	%{name}-Loader = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(spl)

%description ModuleManager
Zend Framework 2.0 introduces a new and powerful approach to modules.
This new module system is designed with flexibility, simplicity, and
re-usability in mind. A module may contain just about anything: PHP
code, including MVC functionality; library code; view scripts; and/or
public assets such as images, CSS, and JavaScript.

%package Mvc
Summary:	Zend Framework 2: MVC Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.mvc.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Form = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Authentication = %{version}-%{release}
Suggests:	%{name}-Config = %{version}-%{release}
Suggests:	%{name}-Console = %{version}-%{release}
Suggests:	%{name}-Di = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-InputFilter = %{version}-%{release}
Suggests:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-Log = %{version}-%{release}
Suggests:	%{name}-ModuleManager = %{version}-%{release}
Suggests:	%{name}-Serializer = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	%{name}-Text = %{version}-%{release}
Suggests:	%{name}-Uri = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	%{name}-Version = %{version}-%{release}
Suggests:	%{name}-View = %{version}-%{release}
Suggests:	php(intl)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Mvc
Zend\Mvc is a brand new MVC implementation designed from the ground up
for Zend Framework 2, focusing on performance and flexibility.

The MVC layer is built on top of the following components:

- Zend\ServiceManager - Zend Framework provides a set of default
  service definitions set up at Zend\Mvc\Service. The ServiceManager
  creates and configures your application instance and workflow.
- Zend\EventManager - The MVC is event driven. This component is used
  everywhere from initial bootstrapping of the application, through
  returning response and request calls, to setting and retrieving routes
  and matched routes, as well as render views.
- Zend\Http - specifically the request and response objects.
- Zend\Stdlib\DispatchableInterface. All "controllers' are simply
  dispatchable objects.

%package Navigation
Summary:	Zend Framework 2: Navigation Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.navigation.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Config = %{version}-%{release}
Suggests:	%{name}-Mvc = %{version}-%{release}
Suggests:	%{name}-Permissions-Acl = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-View = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)

%description Navigation
Zend\Navigation is a component for managing trees of pointers to web
pages. Simply put: It can be used for creating menus, breadcrumbs,
links, and sitemaps, or serve as a model for other navigation related
purposes.

%package Paginator
Summary:	Zend Framework 2: Paginator Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.paginator.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-View = %{version}-%{release}
Suggests:	php(reflection)
Suggests:	php(spl)

%description Paginator
Zend\Paginator is a flexible component for paginating collections of
data and presenting that data to users.

The primary design goals of Zend\Paginator are as follows:

- Paginate arbitrary data, not just relational databases
- Fetch only the results that need to be displayed
- Do not force users to adhere to only one way of displaying data or
  rendering pagination controls
- Loosely couple Zend\Paginator to other Zend Framework components so
  that users who wish to use it independently of Zend\View, Zend\Db,
  etc. can do so

%package Permissions-Acl
Summary:	Zend Framework 2: Permissions ACL Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.permissions.acl.intro.html
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(spl)

%description Permissions-Acl
The Zend\Permissions\Acl component provides a lightweight and flexible
access control list (ACL) implementation for privileges management. In
general, an application may utilize such ACL's to control access to
certain protected objects by other requesting objects.

For the purposes of this documentation:

- a resource is an object to which access is controlled.
- a role is an object that may request access to a Resource.

Put simply, roles request access to resources. For example, if a
parking attendant requests access to a car, then the parking attendant
is the requesting role, and the car is the resource, since access to
the car may not be granted to everyone.

Through the specification and use of an ACL, an application may
control how roles are granted access to resources.

%package Permissions-Rbac
Summary:	Zend Framework 2: Permissions RBAC Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.permissions.rbac.intro.html
Requires:	%{name} = %{version}-%{release}
Suggests:	php(spl)

%description Permissions-Rbac
The Zend\Permissions\Rbac component provides a lightweight role-based
access control implementation based around PHP 5.3's SPL
RecursiveIterator and RecursiveIteratorIterator. RBAC differs from
access control lists (ACL) by putting the emphasis on roles and their
permissions rather than objects (resources).

%package ProgressBar
Summary:	Zend Framework 2: ProgressBar Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.progress-bar.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	php(apc)
Suggests:	php(date)
Suggests:	php(pcre)
Suggests:	php(spl)

%description ProgressBar
Zend\ProgressBar is a component to create and update progress bars in
different environments. It consists of a single backend, which outputs
the progress through one of the multiple adapters. On every update, it
takes an absolute value and optionally a status message, and then
calls the adapter with some precalculated values like percentage and
estimated time left.

%package Serializer
Summary:	Zend Framework 2: Serializer Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.serializer.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Json = %{version}-%{release}
Requires:	%{name}-Math = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(dom)
Suggests:	php(igbinary)
Suggests:	php(pcre)
Suggests:	php(simplexml)
Suggests:	php(spl)
Suggests:	php(xml)

%description Serializer
The Zend\Serializer component provides an adapter based interface to
simply generate storable representation of PHP types by different
facilities, and recover.

Optional: msgpack (php-pecl-msgpack)

%package Server
Summary:	Zend Framework 2: Server Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.server.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Code = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Server
The Zend\Server family of classes provides functionality for the
various server classes, including Zend\XmlRpc\Server and
Zend\Json\Server. Zend\Server\Server provides an interface that mimics
PHP 5's SoapServer class; all server classes should implement this
interface in order to provide a standard server API.

The Zend\Server\Reflection tree provides a standard mechanism for
performing function and class introspection for use as callbacks with
the server classes, and provides data suitable for use with
Zend\Server\Server's getFunctions() and loadFunctions() methods.

%package ServiceManager
Summary:	Zend Framework 2: ServiceManager Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.service-manager.intro.html
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-Di = %{version}-%{release}
Suggests:	php(reflection)
Suggests:	php(spl)

%description ServiceManager
The Service Locator design pattern is implemented by the
Zend\ServiceManager component. The Service Locator is a service/object
locator, tasked with retrieving other objects.

%package Session
Summary:	Zend Framework 2: Session Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-session
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Validator = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(hash)
Suggests:	php(pcre)
Suggests:	php(session)
Suggests:	php(spl)

%description Session
Manage and preserve session data, a logical complement of cookie data,
across multiple page requests by the same client.

Optional: MongoDB (php-pecl-mongo)

%package Soap
Summary:	Zend Framework 2: SOAP Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-soap
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Server = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Uri = %{version}-%{release}
Requires:	php(soap)
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	php(curl)
Suggests:	php(dom)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(simplexml)
Suggests:	php(spl)
Suggests:	php(xml)

%description Soap
%{summary}

%package Stdlib
Summary:	Zend Framework 2: Stdlib Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-stdlib
Requires:	%{name} = %{version}-%{release}
Suggests:	%{name}-EventManager = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-Serializer = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(iconv)
Suggests:	php(intl)
Suggests:	php(json)
Suggests:	php(mbstring)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(spl)

%description Stdlib
%{summary}

%package Tag
Summary:	Zend Framework 2: Tag Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.tag.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Escaper = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)

%description Tag
Zend\Tag is a component suite which provides a facility to work with
taggable Items. As its base, it provides two classes to work with
Tags, Zend\Tag\Item and Zend\Tag\ItemList. Additionally, it comes with
the interface Zend\Tag\TaggableInterface, which allows you to use any
of your models as a taggable item in conjunction with Zend\Tag.

Zend\Tag\Item is a basic taggable item implementation which comes with
the essential functionality required to work with the Zend\Tag suite.
A taggable item always consists of a title and a relative weight (e.g.
number of occurrences). It also stores parameters which are used by
the different sub-components of Zend\Tag.

To group multiple items together, Zend\Tag\ItemList exists as an array
iterator and provides additional functionality to calculate absolute
weight values based on the given relative weights of each item in it.

%package Test
Summary:	Zend Framework 2: Test Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.test.introduction.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Console = %{version}-%{release}
Requires:	%{name}-Dom = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Http = %{version}-%{release}
Requires:	%{name}-Mvc = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-Uri = %{version}-%{release}
Requires:	%{name}-View = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)

%description Test
The Zend\Test component provides tools to facilitate unit testing of
your Zend Framework applications. At this time, we offer facilities to
enable testing of your Zend Framework MVC applications.

PHPUnit is the only library supported currently.

%package Text
Summary:	Zend Framework 2: Text Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/index.html#zend-text
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-ServiceManager = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(pcre)
Suggests:	php(spl)

### TODO: Is Zend/Text/Figlet/zend-framework.flf allowed?

%description Text
%{summary}

%package Uri
Summary:	Zend Framework 2: URI Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.uri.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Escaper = %{version}-%{release}
Requires:	%{name}-Validator = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)

%description Uri
Zend\Uri is a component that aids in manipulating and validating
Uniform Resource Identifiers (URIs) [1]. Zend\Uri exists primarily to
service other components, such as Zend\Http\, but is also useful as a
standalone utility.

URIs always begin with a scheme, followed by a colon. The construction
of the many different schemes varies significantly. The Zend\Uri
component provides the Zend\Uri\UriFactory that returns a class
implementing the Zend\Uri\UriInterface which specializes in the scheme
if such a class is registered with the Factory.

[1] http://www.ietf.org/rfc/rfc3986.txt

%package Validator
Summary:	Zend Framework 2: Validator Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.validator.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Db = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-Math = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Session = %{version}-%{release}
Suggests:	%{name}-Uri = %{version}-%{release}
Suggests:	php(ctype)
Suggests:	php(date)
Suggests:	php(fileinfo)
Suggests:	php(hash)
Suggests:	php(pcre)
Suggests:	php(spl)

%description Validator
The Zend\Validator component provides a set of commonly needed
validators. It also provides a simple validator chaining mechanism by
which multiple validators may be applied to a single datum in a
user-defined order.

%package Version
Summary:	Zend Framework 2: Version Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.version.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	php(pcre)
Suggests:	php(spl)

%description Version
Zend\Version provides a class constant Zend\Version\Version::VERSION
that contains a string identifying the version number of your Zend
Framework installation. Zend\Version\Version::VERSION might contain
"1.7.4', for example.

The static method Zend\Version\Version::compareVersion($version) is
based on the PHP function version_compare(). This method returns -1 if
the specified version is older than the installed Zend Framework
version, 0 if they are the same and +1 if the specified version is
newer than the version of the Zend Framework installation.

%package View
Summary:	Zend Framework 2: View Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.view.quick-start.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-EventManager = %{version}-%{release}
Requires:	%{name}-Loader = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Suggests:	%{name}-Authentication = %{version}-%{release}
Suggests:	%{name}-Escaper = %{version}-%{release}
Suggests:	%{name}-Feed = %{version}-%{release}
Suggests:	%{name}-Filter = %{version}-%{release}
Suggests:	%{name}-Http = %{version}-%{release}
Suggests:	%{name}-I18n = %{version}-%{release}
Suggests:	%{name}-Json = %{version}-%{release}
Suggests:	%{name}-Mvc = %{version}-%{release}
Suggests:	%{name}-Navigation = %{version}-%{release}
Suggests:	%{name}-Paginator = %{version}-%{release}
Suggests:	%{name}-Permissions-Acl = %{version}-%{release}
Suggests:	%{name}-ServiceManager = %{version}-%{release}
Suggests:	%{name}-Uri = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(dom)
Suggests:	php(filter)
Suggests:	php(pcre)
Suggests:	php(spl)

%description View
Zend\View provides the "View' layer of Zend Framework 2's MVC system.
It is a multi-tiered system allowing a variety of mechanisms for
extension, substitution, and more.

%package XmlRpc
Summary:	Zend Framework 2: XML-RPC Component
Group:		Development/Languages/PHP
URL:		http://framework.zend.com/manual/2.4/en/modules/zend.xmlrpc.intro.html
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Http = %{version}-%{release}
Requires:	%{name}-Math = %{version}-%{release}
Requires:	%{name}-Server = %{version}-%{release}
Requires:	%{name}-Stdlib = %{version}-%{release}
Requires:	%{name}-ZendXml = %{version}-%{release}
Suggests:	%{name}-Cache = %{version}-%{release}
Suggests:	php(date)
Suggests:	php(dom)
Suggests:	php(iconv)
Suggests:	php(pcre)
Suggests:	php(reflection)
Suggests:	php(simplexml)
Suggests:	php(spl)
Suggests:	php(xml)
Suggests:	php(xmlwriter)

%description XmlRpc
From its home page, XML-RPC is described as a '...remote procedure
calling using HTTP as the transport and XML as the encoding. XML-RPC
is designed to be as simple as possible, while allowing complex data
structures to be transmitted, processed and returned.'

Zend Framework provides support for both consuming remote XML-RPC
services and building new XML-RPC servers.

[1] http://www.xmlrpc.com/

%package ZendXml
Summary:	Zend Framework 2: XML usage, best practices, and security in PHP
Group:		Development/Languages/PHP
URL:		https://github.com/zendframework/ZendXml
Requires:	%{name} = %{version}-%{release}
Requires:	php(dom)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(xml)

%description ZendXml
This is a security component to prevent XML eXternal Entity (XXE) and
XML Entity Expansion (XEE) attacks on XML documents.

The XXE attack is prevented disabling the load of external entities in
the libxml library used by PHP, using the function
libxml_disable_entity_loader.

The XEE attack is prevented looking inside the XML document for ENTITY
usage. If the XML document uses ENTITY the library throw an Exception.

%prep
%setup -q -n ZendFramework-%{version} %{?with_tests:-a 1}
%patch0 -p2 -d library/Zend/Mail

# move doc for easier install
install -d doc
for p in library/Zend/*/*.json library/Zend/*/*/*.json; do
	p=${p%/composer.json}
	d=${p#library/Zend/}
	install -d doc/$d
	mv $p/*.md $p/composer.json doc/$d
done

%build
%if %{with tests}
cd tests
: Create autoloader for test suite
cat <<'AUTOLOADER' | tee _autoload.php
<?php
require_once '$RPM_BUILD_ROOT%{php_data_dir}/Zend/autoload.php';

Zend\Loader\AutoloaderFactory::factory(array(
	'Zend\\Loader\\StandardAutoloader' => array(
		'namespaces' => array(
		   'ZendTest' => __DIR__ . '/ZendTest',
))));
AUTOLOADER

: ignore these for now
rm ZendTest/Mvc/Controller/Plugin/FilePostRedirectGetTest.php
: PHP 5.4 segfaults https://bugzilla.redhat.com/1131979
rm ZendTest/Serializer/Adapter/WddxTest.php

RET=0
for dir in ZendTest/[A-Z]*; do
	phpunit $dir || RET=1
done
exit $RET
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a library/* $RPM_BUILD_ROOT%{php_data_dir}

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{php_data_dir}/Zend/autoload.php

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%doc *.md composer.json
%dir %{php_data_dir}/Zend

%files Authentication
%defattr(644,root,root,755)
%doc doc/Authentication/*.md
%doc doc/Authentication/composer.json
%{php_data_dir}/Zend/Authentication

%files Barcode
%defattr(644,root,root,755)
%doc doc/Barcode/*.md
%doc doc/Barcode/composer.json
%{php_data_dir}/Zend/Barcode

%files Cache
%defattr(644,root,root,755)
%doc doc/Cache/*.md
%doc doc/Cache/composer.json
%{php_data_dir}/Zend/Cache

%files Captcha
%defattr(644,root,root,755)
%doc doc/Captcha/*.md
%doc doc/Captcha/composer.json
%{php_data_dir}/Zend/Captcha

%files Code
%defattr(644,root,root,755)
%doc doc/Code/*.md
%doc doc/Code/composer.json
%{php_data_dir}/Zend/Code

%files Config
%defattr(644,root,root,755)
%doc doc/Config/*.md
%doc doc/Config/composer.json
%{php_data_dir}/Zend/Config

%files Console
%defattr(644,root,root,755)
%doc doc/Console/*.md
%doc doc/Console/composer.json
%{php_data_dir}/Zend/Console

%files Crypt
%defattr(644,root,root,755)
%doc doc/Crypt/*.md
%doc doc/Crypt/composer.json
%{php_data_dir}/Zend/Crypt

%files Db
%defattr(644,root,root,755)
%doc doc/Db/*.md
%doc doc/Db/composer.json
%{php_data_dir}/Zend/Db

%files Debug
%defattr(644,root,root,755)
%doc doc/Debug/*.md
%doc doc/Debug/composer.json
%{php_data_dir}/Zend/Debug

%files Di
%defattr(644,root,root,755)
%doc doc/Di/*.md
%doc doc/Di/composer.json
%{php_data_dir}/Zend/Di

%files Dom
%defattr(644,root,root,755)
%doc doc/Dom/*.md
%doc doc/Dom/composer.json
%{php_data_dir}/Zend/Dom

%files Escaper
%defattr(644,root,root,755)
%doc doc/Escaper/*.md
%doc doc/Escaper/composer.json
%{php_data_dir}/Zend/Escaper

%files EventManager
%defattr(644,root,root,755)
%doc doc/EventManager/*.md
%doc doc/EventManager/composer.json
%{php_data_dir}/Zend/EventManager

%files Feed
%defattr(644,root,root,755)
%doc doc/Feed/*.md
%doc doc/Feed/composer.json
%{php_data_dir}/Zend/Feed

%files File
%defattr(644,root,root,755)
%doc doc/File/*.md
%doc doc/File/composer.json
%{php_data_dir}/Zend/File

%files Filter
%defattr(644,root,root,755)
%doc doc/Filter/*.md
%doc doc/Filter/composer.json
%{php_data_dir}/Zend/Filter

%files Form
%defattr(644,root,root,755)
%doc doc/Form/*.md
%doc doc/Form/composer.json
%{php_data_dir}/Zend/Form

%files Http
%defattr(644,root,root,755)
%doc doc/Http/*.md
%doc doc/Http/composer.json
%{php_data_dir}/Zend/Http

%files I18n
%defattr(644,root,root,755)
%doc doc/I18n/*.md
%doc doc/I18n/composer.json
%{php_data_dir}/Zend/I18n

%files InputFilter
%defattr(644,root,root,755)
%doc doc/InputFilter/*.md
%doc doc/InputFilter/composer.json
%{php_data_dir}/Zend/InputFilter

%files Json
%defattr(644,root,root,755)
%doc doc/Json/*.md
%doc doc/Json/composer.json
%{php_data_dir}/Zend/Json

%files Ldap
%defattr(644,root,root,755)
%doc doc/Ldap/*.md
%doc doc/Ldap/composer.json
%{php_data_dir}/Zend/Ldap

%files Loader
%defattr(644,root,root,755)
%doc doc/Loader/*.md
%doc doc/Loader/composer.json
%{php_data_dir}/Zend/autoload.php
%{php_data_dir}/Zend/Loader

%files Log
%defattr(644,root,root,755)
%doc doc/Log/*.md
%doc doc/Log/composer.json
%{php_data_dir}/Zend/Log

%files Mail
%defattr(644,root,root,755)
%doc doc/Mail/*.md
%doc doc/Mail/composer.json
%{php_data_dir}/Zend/Mail

%files Math
%defattr(644,root,root,755)
%doc doc/Math/*.md
%doc doc/Math/composer.json
%{php_data_dir}/Zend/Math

%files Memory
%defattr(644,root,root,755)
%doc doc/Memory/*.md
%doc doc/Memory/composer.json
%{php_data_dir}/Zend/Memory

%files Mime
%defattr(644,root,root,755)
%doc doc/Mime/*.md
%doc doc/Mime/composer.json
%{php_data_dir}/Zend/Mime

%files ModuleManager
%defattr(644,root,root,755)
%doc doc/ModuleManager/*.md
%doc doc/ModuleManager/composer.json
%{php_data_dir}/Zend/ModuleManager

%files Mvc
%defattr(644,root,root,755)
%doc doc/Mvc/*.md
%doc doc/Mvc/composer.json
%{php_data_dir}/Zend/Mvc

%files Navigation
%defattr(644,root,root,755)
%doc doc/Navigation/*.md
%doc doc/Navigation/composer.json
%{php_data_dir}/Zend/Navigation

%files Paginator
%defattr(644,root,root,755)
%doc doc/Paginator/*.md
%doc doc/Paginator/composer.json
%{php_data_dir}/Zend/Paginator

%files Permissions-Acl
%defattr(644,root,root,755)
%doc doc/Permissions/Acl/*.md
%doc doc/Permissions/Acl/composer.json
%dir %{php_data_dir}/Zend/Permissions
%{php_data_dir}/Zend/Permissions/Acl

%files Permissions-Rbac
%defattr(644,root,root,755)
%doc doc/Permissions/Rbac/*.md
%doc doc/Permissions/Rbac/composer.json
%dir %{php_data_dir}/Zend/Permissions
%{php_data_dir}/Zend/Permissions/Rbac

%files ProgressBar
%defattr(644,root,root,755)
%doc doc/ProgressBar/*.md
%doc doc/ProgressBar/composer.json
%{php_data_dir}/Zend/ProgressBar

%files Serializer
%defattr(644,root,root,755)
%doc doc/Serializer/*.md
%doc doc/Serializer/composer.json
%{php_data_dir}/Zend/Serializer

%files Server
%defattr(644,root,root,755)
%doc doc/Server/*.md
%doc doc/Server/composer.json
%{php_data_dir}/Zend/Server

%files ServiceManager
%defattr(644,root,root,755)
%doc doc/ServiceManager/*.md
%doc doc/ServiceManager/composer.json
%{php_data_dir}/Zend/ServiceManager

%files Session
%defattr(644,root,root,755)
%doc doc/Session/*.md
%doc doc/Session/composer.json
%{php_data_dir}/Zend/Session

%files Soap
%defattr(644,root,root,755)
%doc doc/Soap/*.md
%doc doc/Soap/composer.json
%{php_data_dir}/Zend/Soap

%files Stdlib
%defattr(644,root,root,755)
%doc doc/Stdlib/*.md
%doc doc/Stdlib/composer.json
%{php_data_dir}/Zend/Stdlib

%files Tag
%defattr(644,root,root,755)
%doc doc/Tag/*.md
%doc doc/Tag/composer.json
%{php_data_dir}/Zend/Tag

%files Test
%defattr(644,root,root,755)
%doc doc/Test/*.md
%doc doc/Test/composer.json
%{php_data_dir}/Zend/Test

%files Text
%defattr(644,root,root,755)
%doc doc/Text/*.md
%doc doc/Text/composer.json
%{php_data_dir}/Zend/Text

%files Uri
%defattr(644,root,root,755)
%doc doc/Uri/*.md
%doc doc/Uri/composer.json
%{php_data_dir}/Zend/Uri

%files Validator
%defattr(644,root,root,755)
%doc doc/Validator/*.md
%doc doc/Validator/composer.json
%{php_data_dir}/Zend/Validator

%files Version
%defattr(644,root,root,755)
%doc doc/Version/*.md
%doc doc/Version/composer.json
%{php_data_dir}/Zend/Version

%files View
%defattr(644,root,root,755)
%doc doc/View/*.md
%doc doc/View/composer.json
%{php_data_dir}/Zend/View

%files XmlRpc
%defattr(644,root,root,755)
%doc doc/XmlRpc/*.md
%doc doc/XmlRpc/composer.json
%{php_data_dir}/Zend/XmlRpc

%files ZendXml
%defattr(644,root,root,755)
%{php_data_dir}/ZendXml
