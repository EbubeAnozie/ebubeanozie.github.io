// Smooth Scroll for Navigation Links
document.querySelectorAll('.navbar a').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute('href')).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    });
  });
  
  // Theme Toggle (Light/Dark Mode)
  const themeToggleBtn = document.createElement('button');
  themeToggleBtn.innerText = 'Switch to Dark Mode';
  themeToggleBtn.classList.add('theme-toggle');
  document.body.appendChild(themeToggleBtn);
  
  themeToggleBtn.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
      themeToggleBtn.innerText = 'Switch to Light Mode';
    } else {
      themeToggleBtn.innerText = 'Switch to Dark Mode';
    }
  });
  
  // Hover Animation for Cards
  const cards = document.querySelectorAll('.card');
  cards.forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'scale(1.05)';
      card.style.transition = 'transform 0.3s ease-in-out';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'scale(1)';
    });
  });
  
  // Slideshow for Profile Image
  let currentImageIndex = 0;
  const profileImages = ['images/ebube1.jpg', 'images/ebube2.jpg', 'images/ebube4.jpg'];
  const profileImage = document.querySelector('img');
  
  function changeProfileImage() {
    profileImage.setAttribute('src', profileImages[currentImageIndex]);
    currentImageIndex = (currentImageIndex + 1) % profileImages.length;
  }
  
  setInterval(changeProfileImage, 5000); // Change image every 5 seconds
  
  // Dynamic Greeting in Footer
  const footer = document.querySelector('footer');
  const greeting = document.createElement('p');
  footer.appendChild(greeting);
  
  function updateGreeting() {
    const currentHour = new Date().getHours();
    let greetingText = '';
  
    if (currentHour >= 5 && currentHour < 12) {
      greetingText = 'Good Morning!';
    } else if (currentHour >= 12 && currentHour < 18) {
      greetingText = 'Good Afternoon!';
    } else {
      greetingText = 'Good Evening!';
    }
  
    greeting.textContent = greetingText;
  }
  
  updateGreeting(); // Set initial greeting
  setInterval(updateGreeting, 3600000); // Update greeting every hour
