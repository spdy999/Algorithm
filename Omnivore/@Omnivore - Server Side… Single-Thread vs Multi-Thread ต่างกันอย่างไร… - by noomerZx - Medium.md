---
id: 4b742c0d-5b5d-41ed-8d47-3e79c0640809
---

# Server Side… Single-Thread vs Multi-Thread ต่างกันอย่างไร… | by noomerZx | Medium
#Omnivore

[Read on Omnivore](https://omnivore.app/me/https-noomerzx-medium-com-server-side-single-thread-vs-multi-thr-1906e281041)
[Read Original](https://noomerzx.medium.com/server-side-single-thread-vs-multi-thread-%E0%B8%95%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B8%81%E0%B8%B1%E0%B8%99%E0%B8%AD%E0%B8%A2%E0%B9%88%E0%B8%B2%E0%B8%87%E0%B9%84%E0%B8%A3-c22e9703068e)

## Highlights

> (Event-Loop) [⤴️](https://omnivore.app/me/https-noomerzx-medium-com-server-side-single-thread-vs-multi-thr-1906e281041#b46117b1-a834-4d0c-96bf-20f483b3da9c)  ^b46117b1


---
credit: <https://www.backblaze.com/blog/whats-the-diff-programs-processes-and-threads/>

ห่างหายไปนาน เนื่องจากอาการป่วยเรื้อรัง วันนี้พอมีเวลาเลยจะมาเล่าสู่กันฟังเรื่อง Single-Thread กับ Multi-Thread และทำไมเรื่องนี้มันถึงทำให้ Node.js เฟื่องฟูขึ้นมาในช่วงหลังๆ

ยกตัวอย่างภาษาที่ใกล้ตัวที่สุดอย่าง JavaScript หรือ Node.js นั้นเป็นการทำงานแบบ Single-Thread และภาษายอดนิยมในสมัยก่อนอย่าง PHP นั้นมีการทำงานแบบ Multi-Thread เดี๋ยวเรามาลองดูกันว่ามันทำงานต่างกันอย่างไร และข้อดีข้อเสียของแต่ละแบบคืออะไร

## Single-Thread ==(Event-Loop)==

มาเริ่มกันที่ฝั่งของ Single-Thread กันก่อน ขอยกตัวอย่างจาก Node.js ซึ่งโดยปกติแล้วเราจะต้อง Run Application ขึ้นมาก่อน โดยมันก็จะมีการกิน CPU & RAM ในระดับหนึ่ง จากนั้นตัว Node.js ใช้ความสามารถของ Event Loop ในการรับ request ที่เข้ามา ซึ่งนั่นเป็นเบื้องหลังว่าทำไม Single-Thread Applicatyion ถึงรองรับ request แบบ parallel ได้ มันทำงานยังไงลองดูตามนี้โลด

request1 -> make db request1  
request2 -> make db request2  
request3 -> make db request3  
db? response -> request? send response  
db? response -> request? send response  
db? response -> request? send response

ซึ่งภาระส่วนใหญ่จะไปตกอยู่ที่ Database เป็นหลัก เพราะเมื่อยิง Database Request ออกไปตัว Application ก็จะสามารถไป process งานอื่นๆต่อได้ทันที ซึ่งก็ไม่ได้หนักมากทำให้การทำงานของ CPU แทบจะไม่ได้มีผลกระทบใดๆเลย และตัว DB Engine เองก็ทำงานแบบ Multi-Thread อยู่แล้วนั่นเอง

ถ้าใครยังไม่ค่อยเข้าใจเรื่อง Event-Loop [คลิก](https://stories.sellsuki.co.th/js-101-%E0%B8%9E%E0%B8%B7%E0%B9%89%E0%B8%99%E0%B8%90%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%88-%E0%B8%95%E0%B9%89%E0%B8%AD%E0%B8%87%E0%B8%AB%E0%B9%89%E0%B8%B2%E0%B8%A1-%E0%B8%9E%E0%B8%A5%E0%B8%B2%E0%B8%94-bac5de6f9900) อ่านช่วงท้ายๆ

## ข้อดี

กิน Memory น้อยเพราะไม่ต้อง Spawn Thread ใหม่ในทุกๆ request และเมื่อใช้ Memory น้อยก็ทำให้รับ request ได้เยอะขึ้ัน

## ข้อเสีย

1. เมื่อเราต้องทำงานที่ต้องใช้ CPU หนักๆจะทำให้การทำงานโดยรวมช้าลง ตัวอย่างงานที่ใช้ CPU เยอะๆ เช่น render3D, encode music file อะไรทำนองนี้
2. ตามชื่อของมันเลยครับ Single-Thread มันทำงานบน Single-Core CPU ทำให้ต่อให้เครื่องคุณมี 10–20 Core ก็ไม่ทำให้ Single-Thread Application ของคุณทำงานได้เร็วหรือแรงขึ้นเลย…
3. เมื่อมี Request ใดที่ทำให้ Application Failed อาจทำให้ Request อื่นๆไม่สามารถ Process ต่อได้หรืออาจกระทบกับทั้งระบบให้ไม่สามารถรับ Request ต่อๆไปได้ ซึ่งต้องทำการ Restart Application ใหม่

> Single-Thread (Event Loop) เปรียบเสมือนร้านขายชานม ที่มีพนักงานคนเดียว คุณสามารถสั่งชาและรับบัตรคิวเอาไว้ และเดินไปไหนก็ได้ เมื่อพร้อมดื่มพนักงานจะโทรเรียกเอง ไม่ต้องยืนรอ

## Multi-Thread

มาถึงตรงนี้หลายๆคนอาจจะสงสัยว่า Single-Thread มีข้อเสียเยอะมาก แต่ทำไม Node.js ถึงมานิยมมากขึ้นในช่วงหลังๆ มาครับเรามาลองดูทางฝั่ง Multi-Thread กันบ้างดีกว่าว่ามันทำงานยังไง

request1 -> spawn thread -> make db request & wait -> send response  
request2 -> spawn thread -> make db request & wait -> send response  
request3 -> spawn thread -> make db request & wait -> send response

จะเห็นว่าในทุก Request จะมีการ Spawn Thread ใหม่เสมอ แต่การทำงานส่วนใหญ่ก็จะยังไปลงกับ Database Request ทำให้การทำงานของ CPU จะไม่ได้แตกต่างกับ Single-Thread มากนัก แต่ก็จำเป็นจะต้องจอง Memory สำหรับการทำงานในแต่ละ Thread แยกออกจากกัน ซึ่งอาจจะไม่ได้ใช้เยอะมากเหมือนกัน Start Application แต่มันก็ไม่น้อยนะเอ้อ

## ข้อดี

แต่ละ Thread ทำงานแยกจากกันทำให้ถ้า Thread ใดตาย ก็จะไม่กระทบกับการทำงาน Thread หรือ Request อื่นๆ

## ข้อเสีย

1. เมื่อแต่ละ Thread จะต้องทำการจอง Memory ของตัวเอง ลองนึกสภาพว่าถ้ามี Request เข้ามาเยอะๆ และแต่ละ Request/Thread จะต้องจอง Memory สำหรับตัวแปรต่างๆอีกคิดดูว่าจะมีการใช้งาน Memory มหาศาลขนาดไหน ซึ่งเมื่อ Memory ถูกใช้เยอะ ก็จะทำให้จำนวน Request ที่รับได้นั้นน้อยลงไปด้วย
2. ลองมานึกถึงภาษาที่ต้องมีการ Process ก่อนอย่าง PHP ก็จะยิ่งทำให้เปลือง Memory เข้าไปอีกเพราะต้องแบ่งไปให้ PHP Runtime ในการทำงานด้วยนั่นเอง

> Multi Thread เปรียบเสมือนร้านขายชานม ที่มีพนักงานขายหลายคน สามารถรับลูกค้าได้พร้อมกันมากกว่า 1 คน แต่ลูกค้าจะต้องต่อคิวรอรับชาในทันทีและห้ามออกจากแถวไปก่อน

## Scaling

จากที่ผมอธิบายไปข้างต้นจะเห็นว่าจริงๆแล้วมันไม่ได้มีใครที่ชนะกันอย่างขาดลอย เพียงแต่ว่าในทรัพยากรที่จำกัด Single-Thread ของ Node.js จะทำงานได้มีประสิทธิภาพกว่านั่นเอง นั่นเป็นเหตุผลว่าทำไมมันถึงเริ่มนิยมขึ้นมาในช่วง 3–4 ปีหลังมานี้นั่นเอง

แต่จริงๆแล้วการ Scaling ก็จะเข้ามาช่วยแก้ปัญหาของทั้ง 2 แบบได้ แต่เราก็จะต้องเลือกให้ถูกวิธีด้วยเช่นกัน ซึ่งสามารถทำได้หลายแบบทั้ง Vertical/Horizontal Scaling

**Multi-Thread** สามารถคั่นด้วย Gateway/Load Balance ที่ทำตัวเองเป็น Event Loop ในการ Handle Request อย่าง nginx หรือทางเลือกสุดท้าย คือ “เงิน” แก้ปัญหาได้ทุกสิ่ง อัด CPU Core และ Memory เข้าไปเยอะๆ

**Single-Thread** เองก็มีทางแก้มากมาย เช่น แทนที่จะหาทางให้มันทำ Multi-Thread เราก็ Run Application ไว้หลายๆตัวตามจำนวน Core แทนแล้วเอา Load Balance มาคั่นอีกที หรือถ้าใช้ Cloud Provider ในปัจจุบันยิ่งเหมาะ เปิดเครื่องเล็กๆหลายๆเครื่อง ยิ่งสมัยนี้มี Auto-Scaling ทำจะ Spawn เครื่องและ Start Application ให้เองเมื่อถึง limit ที่ตั้งไว้ พร้อมเอา Load Balance มาจิ้มให้อีก หรือสุดท้ายก็ใช้ “เงิน” แก้เหมือนเดิมเปิดเครื่องทิ้งไว้เลยหลายๆเครื่องแล้วเอา Load Balance จิ้มค้างไว้เลยไม่ต้องวุ่นวาย

## สรุป

ก็จบกันไปแล้วครับมาเล่าสู่กันฟังคร่าวๆ ระหว่าง Single-Thread vs Multi-Thread ซึ่งตรงไหนผิดพลาดประการใดก็ ติชม แนะนำ เป็นความรู้เพิ่มเติมได้เหมือนเดิมครับ

## References

* <https://stackoverflow.com/questions/34855352/how-in-general-does-node-js-handle-10-000-concurrent-requests?fbclid=IwAR1084JkXJaRntFTYn53ski5pC5s0qYTkCaJgNbNlEkeb4DApHaMsSnYbns>
