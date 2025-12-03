import { useEffect } from 'react';

function Home() {
  useEffect(() => {
    const anchors = document.querySelectorAll('a[href^="#"]');

    const handleClick = (e) => {
      const targetSelector = e.currentTarget.getAttribute('href');
      if (!targetSelector || targetSelector === '#') return;

      const target = document.querySelector(targetSelector);
      if (!target) return;

      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    };

    anchors.forEach((anchor) => anchor.addEventListener('click', handleClick));

    const cards = document.querySelectorAll('.service-card');
    cards.forEach((card) => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'all 0.6s ease';
    });

    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -100px 0px',
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, observerOptions);

    cards.forEach((card) => observer.observe(card));

    return () => {
      anchors.forEach((anchor) => anchor.removeEventListener('click', handleClick));
      observer.disconnect();
    };
  }, []);

  return (
    <>
      <section className="hero" id="home">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <div className="hero-content">
          <h1>AI Automation That Works For You</h1>
          <p>
            Transform your business with intelligent workflows, custom AI agents, and seamless automation
            solutions designed for the modern world.
          </p>
          <div className="hero-buttons">
            <a href="/contact" className="cta-button">
              Start Automating
            </a>
            <a href="#services" className="secondary-button">
              Explore Solutions
            </a>
          </div>
        </div>
      </section>

      <section className="services" id="services">
        <div className="section-header">
          <h2>Our Services</h2>
          <p>Cutting-edge AI solutions tailored to your needs</p>
        </div>
        <div className="services-grid">
          <div className="service-card">
            <div className="service-icon">🤖</div>
            <h3>AI Agents</h3>
            <p>
              Custom AI agents that understand your business context and automate complex decision-making
              processes with precision.
            </p>
          </div>
          <div className="service-card">
            <div className="service-icon">⚡</div>
            <h3>Workflow Automation</h3>
            <p>
              Streamline your operations with intelligent workflows that connect your tools and eliminate
              repetitive tasks.
            </p>
          </div>
          <div className="service-card">
            <div className="service-icon">🔗</div>
            <h3>Integration Solutions</h3>
            <p>
              Seamlessly connect your existing systems with AI-powered bridges that enhance functionality and
              data flow.
            </p>
          </div>
        </div>
      </section>

      <section className="features" id="features">
        <div className="features-content">
          <div className="features-text">
            <h2>Why Choose Azul?</h2>
            <div className="feature-item">
              <div className="feature-icon">✨</div>
              <div>
                <h3>State-of-the-Art AI</h3>
                <p>Leverage the latest AI technologies to stay ahead of the competition.</p>
              </div>
            </div>
            <div className="feature-item">
              <div className="feature-icon">🎯</div>
              <div>
                <h3>Custom Solutions</h3>
                <p>Every automation is tailored to your specific business requirements.</p>
              </div>
            </div>
            <div className="feature-item">
              <div className="feature-icon">🚀</div>
              <div>
                <h3>Rapid Deployment</h3>
                <p>Get up and running quickly with our efficient implementation process.</p>
              </div>
            </div>
          </div>
          <div className="features-visual">
            <div className="visual-box">🌊</div>
          </div>
        </div>
      </section>

      <section className="cta-section" id="contact-section">
        <h2>Ready to Transform Your Business?</h2>
        <p>Join the AI revolution and automate your way to success</p>
        <a href="/contact" className="cta-button">
          Get In Touch
        </a>
      </section>
    </>
  );
}

export default Home;
