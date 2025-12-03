import { useState } from 'react';

const API_BASE = import.meta.env.VITE_API_BASE || '';

const faqItems = [
  {
    q: 'How quickly can you implement an automation solution?',
    a: 'Implementation time varies based on complexity, but most projects are completed within 2-6 weeks. Simple automations can be deployed in just a few days.',
  },
  {
    q: 'Do you offer ongoing support?',
    a: 'Yes! We provide comprehensive support packages including monitoring, updates, and optimization to ensure your automations continue running smoothly.',
  },
  {
    q: 'Can you integrate with our existing tools?',
    a: 'Absolutely! We specialize in creating seamless integrations with popular business tools and can work with custom APIs and legacy systems.',
  },
  {
    q: 'What industries do you serve?',
    a: 'We work with businesses across all industries including finance, healthcare, e-commerce, manufacturing, and professional services.',
  },
];

function Contact() {
  const [activeFaq, setActiveFaq] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const [successVisible, setSuccessVisible] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');

  const handleFaqToggle = (index) => {
    setActiveFaq((prev) => (prev === index ? null : index));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage('');
    setSubmitting(true);

    const formData = new FormData(e.target);
    const payload = {
      name: formData.get('name'),
      email: formData.get('email'),
      phone_number: formData.get('phone') || '',
      company_name: formData.get('company') || '',
      service_interest: formData.get('service'),
      message: formData.get('message'),
    };

    try {
      const response = await fetch(`${API_BASE}/api/customers`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      let data = {};
      try {
        data = await response.json();
      } catch {
        data = {};
      }

      if (response.ok) {
        // success
        setSuccessVisible(true);
        e.target.reset();
        setTimeout(() => setSuccessVisible(false), 5000);
      } else if (response.status === 422) {
        let msg = 'Please check your information:\n';
        if (data.detail) {
          if (Array.isArray(data.detail)) {
            data.detail.forEach((error) => {
              msg += `- ${error.msg || error.message}\n`;
            });
          } else if (typeof data.detail === 'string') {
            msg = data.detail;
          } else if (data.detail.msg) {
            msg = data.detail.msg;
          }
        } else if (data.message) {
          msg = data.message;
        }
        setErrorMessage(msg);
      } else if (response.status === 409) {
        setErrorMessage(
          'This email address is already registered. Please use a different email or contact us directly.'
        );
      } else {
        setErrorMessage(
          'Something went wrong. Please try again later or contact us directly at contact@azulworkflows.com'
        );
      }
    } catch (error) {
      console.error('Network error:', error);
      setErrorMessage(
        'Unable to connect to the server. Please check your internet connection and try again.'
      );
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <>
      <section className="contact-hero">
        <div className="shape shape-1"></div>
        <div className="shape shape-2"></div>
        <h1>Let&apos;s Build Something Amazing</h1>
        <p>Ready to transform your business with AI? We&apos;re here to help you every step of the way.</p>
      </section>

      <section className="contact-section">
        <div className="contact-container">
          <div className="contact-form">
            <h2>Send Us a Message</h2>
            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="name">Name</label>
                <input type="text" id="name" name="name" required />
              </div>
              <div className="form-group">
                <label htmlFor="email">Email Address</label>
                <input type="email" id="email" name="email" required />
              </div>
              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="phone">Phone Number (Optional)</label>
                  <input type="tel" id="phone" name="phone" placeholder="+1 (234) 567-890" />
                </div>
                <div className="form-group">
                  <label htmlFor="company">Company Name (Optional)</label>
                  <input type="text" id="company" name="company" />
                </div>
              </div>
              <div className="form-group">
                <label htmlFor="service">Service Interest</label>
                <select id="service" name="service" required>
                  <option value="">Select a service</option>
                  <option value="AI Agents">AI Agents</option>
                  <option value="Workflow Automation">Workflow Automation</option>
                  <option value="Integration Solutions">Integration Solutions</option>
                  <option value="Consulting">Consulting</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div className="form-group">
                <label htmlFor="message">Your Message</label>
                <textarea
                  id="message"
                  name="message"
                  required
                  placeholder="Tell us about your project or automation needs..."
                ></textarea>
              </div>
              <button type="submit" className="submit-btn" disabled={submitting}>
                {submitting ? 'Sending...' : 'Send Message'}
              </button>
            </form>
          </div>

          <div className="contact-info">
            <h2>Get In Touch</h2>

            <div className="info-item">
              <div className="info-icon">📧</div>
              <div className="info-content">
                <h3>Email Us</h3>
                <p>
                  <a href="mailto:contact@azulworkflows.com">contact@azulworkflows.com</a>
                </p>
              </div>
            </div>

            <div className="info-item">
              <div className="info-icon">📱</div>
              <div className="info-content">
                <h3>Call Us</h3>
                <p>
                  <a href="tel:+1234567890">+1 (234) 567-890</a>
                </p>
              </div>
            </div>

            <div className="info-item">
              <div className="info-icon">🕐</div>
              <div className="info-content">
                <h3>Business Hours</h3>
                <p>Monday - Friday: 9:00 AM - 6:00 PM EST</p>
              </div>
            </div>

            <div className="info-item">
              <div className="info-icon">🌍</div>
              <div className="info-content">
                <h3>Location</h3>
                <p>Serving clients globally with remote-first solutions</p>
              </div>
            </div>
          </div>
        </div>

        <div className="faq-section">
          <h2>Frequently Asked Questions</h2>
          {faqItems.map((item, index) => {
            const isActive = activeFaq === index;
            return (
              <div className="faq-item" key={index}>
                <div className="faq-question" onClick={() => handleFaqToggle(index)}>
                  <span>{item.q}</span>
                  <span className={`faq-toggle ${isActive ? 'active' : ''}`}>+</span>
                </div>
                <div className={`faq-answer ${isActive ? 'active' : ''}`}>
                  <p>{item.a}</p>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <div className={`success-message ${successVisible ? 'show' : ''}`}>
        Thank you for your message! We&apos;ve sent a confirmation email to your address. Please check your spam
        or junk folder if you don&apos;t see it in your inbox.
      </div>

      <div className={`error-message ${errorMessage ? 'show' : ''}`}>
        <pre>{errorMessage}</pre>
      </div>
    </>
  );
}

export default Contact;
