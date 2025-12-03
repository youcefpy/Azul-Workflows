import { NavLink, useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';

function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const onScroll = () => {
      setScrolled(window.scrollY > 50);
    };
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  const navClass = scrolled ? 'scrolled' : '';

  return (
    <nav id="navbar" className={navClass}>
      <div className="nav-container">
        <NavLink to="/" className="logo">
          Azul Workflows
        </NavLink>
        <div className="nav-links">
          {location.pathname === '/' ? (
            <>
              <a href="#home">Home</a>
              <a href="#services">Services</a>
              <a href="#features">Features</a>
            </>
          ) : (
            <>
              <NavLink to="/" className={({ isActive }) => (isActive ? 'active-link' : '')}>
                Home
              </NavLink>
              <NavLink to="/#services">Services</NavLink>
              <NavLink to="/#features">Features</NavLink>
            </>
          )}
          <NavLink
            to="/contact"
            className={({ isActive }) =>
              'cta-button' + (isActive ? ' active-contact' : '')
            }
          >
            Get Started
          </NavLink>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
