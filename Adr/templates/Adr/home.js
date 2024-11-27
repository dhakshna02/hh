#init{
    margin-top: 2rem;
    background:  rgba(34, 70, 76, 0);
    position: relative;
    padding: 10px 20px;
    border-radius: 7px;
    border: 1px solid rgba(82, 174, 154, 0.7);
    font-size: 14px;
    width: 300px;
    font-weight: 600;
    letter-spacing: 2px;
    color: aliceblue;
    cursor: pointer;
    margin-top: 80%;
    margin-left: -0%;
    Z-index:4;
    
    
    }
    .desc p{
    color: rgb(133,153,168);
    margin: 0;
    font-weight: 600;
    }
    .text{
    font-size: 65px;
    font-weight: 800;
    color: rgb(172, 190, 190);
    margin: 0;
    }
    .parent{
    position: relative;
    height: 100%;
    padding: 0 7rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    }
    .bot-img{
    width: 20rem;
    height: 20rem;
    }
    .child{
    box-shadow: 0 0 2px rgb(4, 1, 0);
    border-radius: 15px;
    height: 30rem;
    width: 16rem;
    margin-right:10px;
    background: rgba(156, 15, 15, 0);
    }
    .header img{
    width: 35px;
    height: 35px;
    border-radius: 50%;
    margin: 0 0.5rem;
    border: 1px solid rgb(231,231,231);
    padding: 5px;
    }
    .header{
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    border-bottom: 1px solid rgba(245, 245, 245, 0.504);
    background: rgb(37, 65, 65);
    width: 370px;
    padding: 5px 0;
    border-top-right-radius: 15px;
    border-top-left-radius: 15px;
    z-index: 1;
    box-shadow: 0 0 2px rgb(201, 238, 238);
    }
    .h-child{
    display: flex;
    align-items: center;
    }
    .header span{
    font-size: 13px;
    margin: 0;
    padding: 0;
    }
    .refBtn{
    position: absolute;
    bottom: 1rem;
    right: 1rem;
    background: none;
    border: none;
    border-radius: 50%;
    color: rgb(119, 112, 112);
    font-size: 18px;
    cursor: pointer;
    
    }
    .name{
    font-weight: 600;
    color: #f9fafc;
    }
    .footer{
    position: absolute;
    bottom: 0;
    width: 370px;
    background: rgb(37, 65, 65);
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
    color: #f9fafcab;
    padding: 15px 0;
    text-align: center;
    font-size: 14px;
    box-shadow: 0 0 3px rgb(208, 239, 241);
    }
    #chat-box{
    
    top: 0px;
    padding: 8px 10px;
    font-size: 12px;
    height: 24.2rem;
    overflow: auto;
    background: rgb(23, 23, 24);
    text-align: center;
    width: 370px;
    align-items: left;
    }
    
    
    /* these classes will be used in javascript file */
    .msg{
    background: rgba(176, 228, 222, 0.874);
    padding: 5px 15px;
    border-top-right-radius: 15px;
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
    width: max-content;
    font-size: 14px;
    color: #2d4f49;
    box-shadow: 0 0 5px rgb(130, 220, 211);
    max-width: 65%;
    text-align: justify; 
    margin-top: 20px;
    }
    .test{
    text-align: right;
    margin: 20px 0;
    }
    .rep{
    background: rgb(253,243,224);
    color: lightslategray;
    padding: 5px 15px;
    border-top-right-radius: 15px;
    border-bottom-left-radius: 15px;
    border-top-left-radius: 15px;
    font-size: 14px;
    box-shadow: 0 0 5px rgb(211,211,211);
    }
    .opt{
    padding: 5px 20px;
    columns: rgb(122, 255, 255);
    border: 1px solid rgb(213, 230, 229);
    border-radius: 1rem;
    margin: 0.3rem 0.5rem;
    display: inline-block;
    cursor: pointer;
    font-weight: 500;
    background: white;
    text-align: justify;
    font-size: 14px;
    color: rgb(22, 49, 50);
    }

    <button id="init" >Mr. ADR'Bot</button>

  <div id="test" style="position: relative; margin-top:0%;display: none; margin-right:40%">
      <div class="child" id="chatbot" style="position: relative;">
          <div class="header" style="position: relative;">
              <div class="h-child"   style="position: relative;">
                  <img src="images/profile.jpg" alt="avatar" id="avatar">
                  <div>
                      <span class="name">Chatbot</span>
                      <br>
                      <span style="color:lawngreen">online</span>
                  </div>
              </div>
              <div>
                  <button class="refBtn"><i class="fa fa-refresh" onclick="initChat()"></i></button>
              </div>
          </div>

          <div id="chat-box" style="position: relative;">

          </div>
          <div class="footer">
              <span>powered by @adrgrp
              </span>
          </div>
      </div>
  </div>

  </div>
  <script>
    function animateCounter(counterElement, upto) {
    let count = 0;
    let counts = setInterval(function() {
      count++;
      counterElement.innerHTML = count;
    
      // Add a "+" symbol after every 4 counts
      if (count % 5 === 0) {
          counterElement.innerHTML += " +";
      }
    
      counterElement.classList.add('animate');
      setTimeout(() => counterElement.classList.remove('animate'), 100);
    
      if (count === upto) {
          clearInterval(counts);
      }
    }, 10);
    }
    
    animateCounter(document.getElementById("counter1"),50);
    animateCounter(document.getElementById("counter2"), 30);
    animateCounter(document.getElementById("counter3"), 20);
    animateCounter(document.getElementById("counter4"), 100);
    
    </script>
    
    </div>
    <div>
    <div class="logos">
    <span class="clients-title" style="font-size: 3rem; margin-left: 450px;" data-aos="fade-up">
      Our Customers
    </span>
    <h1 class="clients-head" style="text-align: center;" data-aos="fade-up" data-aos-delay="100">
      Driving technology for leading brands
    </h1>
      <div class="logo_items">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/HT_log.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/Kar_tech.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/expleo.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/hacket.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/QK_Logo.webp"> <img src="https://adrgrp.com/wp-content/uploads/2024/07/HT_log.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/Kar_tech.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/expleo.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/hacket.webp">
      <img src="https://adrgrp.com/wp-content/uploads/2024/07/QK_Logo.webp">
      
      </div>
      <div class="logo_items">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/HT_log.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/Kar_tech.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/expleo.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/hacket.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/QK_Logo.webp"> <img src="https://adrgrp.com/wp-content/uploads/2024/07/HT_log.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/Kar_tech.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/expleo.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/hacket.webp">
        <img src="https://adrgrp.com/wp-content/uploads/2024/07/QK_Logo.webp">
      
      
      </div>
    </div>
    </div>
    
    
    
    <script >
    