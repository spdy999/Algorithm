# macOS Forensics: The Basics

![rw-book-cover](https://tryhackme.com/img/meta/default.png)

## Metadata
- Author: [[TryHackMe]]
- Full Title: macOS Forensics: The Basics
- Category: #articles
- Document Tags: [[CyberSec]] 
- Summary: macOS is Apple's operating system for computers and holds a 14% market share in the desktop and laptop market. It has evolved from the classic MacOS to MacOS X and now macOS, with significant changes like the introduction of the Apple File System (APFS) in 2017. Steve Jobs played a key role in reviving Apple and transforming its operating system into a Unix-like platform.
- URL: https://tryhackme.com/room/macosforensicsbasics

## Full Document
Task 1

Introduction

Task 2

A Brief History of macOS

macOS is Apple's operating system for desktop and laptop systems and is the 2nd most used operating system for desktops and laptops after Microsoft Windows. As of December 2024, macOS has a roughly [14% market share](https://gs.statcounter.com/os-market-share/desktop/worldwide/#monthly-202402-202402-bar) among desktop and laptop OS worldwide, significantly higher than Linux distributions. Previously, macOS has had a tumultuous history, going almost extinct once.

#### The Start of Apple's Journey

Steve Jobs founded Apple Computer in 1976 with Steve Wozniak and Ronald Wayne as partners. Apple's first computer was named Apple I, followed by Apple II and Apple III in the following years. In the early 1980s, Apple released Lisa, one of the first computers using a graphical user interface (GUI), after being inspired by the technology developed by Xerox. However, Lisa had some teething problems, which caused trouble for Apple. Some of these problems were addressed in the Macintosh, which had promising sales initially but was soon overcome by other PC vendors who overtook the market. During this time, Steve Jobs was forced out of Apple, founding Pixar and NeXT Computer. In Jobs' absence, Apple was a shadow of its former self and could only revive itself after Jobs' return.

![A timeline of major events in macOS history](https://tryhackme-images.s3.amazonaws.com/user-uploads/61306d87a330ed00419e22e7/room-content/61306d87a330ed00419e22e7-1743186548422.png)A timeline of major events in macOS history
#### The Return of Jobs

Apple acquired Steve Jobs' new venture, NeXT Computer, in 1998, bringing him back to the driving seat of Apple. MacOS 8.1 was released in the same year, and the Hierarchical File System Plus (HFS+) was introduced as the main file system in macOS, replacing the previous HFS file system. We will learn about the HFS+ file system in the coming tasks. This file system was the mainstay of macOS until it was replaced by APFS in 2017.

#### NeXTSTEP and MacOS X

In 2001, the classic MacOS was replaced by MacOS X, a Unix-like operating system derived from the NeXTSTEP OS from NeXT Computer. Introducing the Unix-like operating system caused some problems for the HFS+ file system, which did not support features such as hard linking and permissions. These features were added to the file system to ensure compatibility, which has helped the file system remain relevant for a long time.

#### MacOS X, OS X and macOS

MacOS versions up to MacOS 9 are considered classic macOS now. MacOS 10 was branded by Apple as MacOS X, using the Roman numeral X for the number ten. Following MacOS X, Apple incremented just the minor version numbers for each new MacOS release, keeping the major version as 10, therefore releasing MacOS 10.1, 10.2, 10.3, and so on. In 2012, Apple removed the word 'Mac' from the MacOS X and rebranded the OS as simply OS X for version 10.8, Mountain Lion. In 2016, the OS name was rebranded as macOS with the release of the macOS Sierra (macOS 10.12). This seemed an effort to remain consistent with different OS variants for Apple products, such as watchOS, iOS, tvOS, and iPadOS. However, Apple kept using macOS 10.xx version numbers till the release of macOS Big Sur, which uses macOS 11 as the version number. Since then, every new macOS version has been an increment to the significant OS version, so after macOS 11, we got macOS 12 (Monterey), and so on. Previewed in macOS 10.12 Sierra and starting from macOS 10.13 High Sierra, Apple has been using the new Apple File System (APFS). APFS brought many improvements holding macOS back due to the limitations of the HFS+ file system, such as better support for SSDs, better security features, and overall bringing macOS file systems to the new age. APFS is now the file system used for all Apple devices, including Apple Watch, iPhone, Apple TV, and iPad.

Answer the questions below

Task 4

APFS File System

Task 5

macOS Directory Structure and Domains

Task 6

macOS File Formats

Task 7

Challenges in Data Acquisition

Task 8

Mounting APFS Disk Image

Task 9

Conclusion
