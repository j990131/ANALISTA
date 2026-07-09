import React, { useState } from "react";
import "./DentalPromoPage.css";

const products = [
  {
    id: 1,
    name: "Kit Blanqueador",
    description: "Blanqueamiento profesional en casa",
    price: "$24.00",
    emoji: "🦷",
    color: "#E8F4FD",
    accent: "#4A90D9",
  },
  {
    id: 2,
    name: "Cepillo Sónico",
    description: "5 modos de limpieza intensa",
    price: "$18.00",
    emoji: "🪥",
    color: "#EAF9F1",
    accent: "#27AE60",
  },
  {
    id: 3,
    name: "Irrigador Oral",
    description: "Limpieza profunda interdental",
    price: "$32.00",
    emoji: "💧",
    color: "#EEF2FF",
    accent: "#6C63FF",
  },
  {
    id: 4,
    name: "Protector Bucal",
    description: "Protección nocturna premium",
    price: "$15.00",
    emoji: "😁",
    color: "#FFF5E4",
    accent: "#F5A623",
  },
];

export default function DentalPromoPage() {
  const [activeIndex, setActiveIndex] = useState(0);

  const getCardStyle = (index) => {
    const offset = index - activeIndex;
    const absOffset = Math.abs(offset);

    // Diagonal layout: each card shifts right and down
    const translateX = offset * 90 + offset * 10;
    const translateY = offset * 40;
    const rotate = offset * 8;
    const scale = absOffset === 0 ? 1 : absOffset === 1 ? 0.82 : 0.65;
    const zIndex = products.length - absOffset;
    const opacity = absOffset > 2 ? 0 : 1 - absOffset * 0.15;

    return {
      transform: `translateX(${translateX}px) translateY(${translateY}px) rotate(${rotate}deg) scale(${scale})`,
      zIndex,
      opacity,
      transition: "all 0.45s cubic-bezier(0.34, 1.56, 0.64, 1)",
    };
  };

  const next = () => setActiveIndex((i) => (i + 1) % products.length);
  const prev = () =>
    setActiveIndex((i) => (i - 1 + products.length) % products.length);

  const active = products[activeIndex];

  return (
    <div className="promo-page">
      {/* Static background */}
      <div className="promo-bg">
        <div className="bg-arch" />
        <div className="bg-dots" />
      </div>

      {/* Header */}
      <header className="promo-header">
        <span className="header-star">✦</span>
        <p className="header-only">Solo Este</p>
        <h1 className="header-title">Fin de Semana</h1>
      </header>

      {/* Diagonal Carousel */}
      <div className="carousel-stage">
        <div className="carousel-track">
          {products.map((product, index) => (
            <div
              key={product.id}
              className={`product-card ${index === activeIndex ? "active" : ""}`}
              style={getCardStyle(index)}
              onClick={() => setActiveIndex(index)}
            >
              <div
                className="card-inner"
                style={{ background: product.color }}
              >
                <div
                  className="card-icon-bg"
                  style={{ background: product.accent + "22" }}
                >
                  <span className="card-emoji">{product.emoji}</span>
                </div>
                <div className="card-badge" style={{ color: product.accent }}>
                  DENTAL PRO
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Navigation arrows */}
        <button className="nav-btn nav-prev" onClick={prev} aria-label="Producto anterior">
          ‹
        </button>
        <button className="nav-btn nav-next" onClick={next} aria-label="Producto siguiente">
          ›
        </button>
      </div>

      {/* Active Product Info */}
      <div className="product-info" aria-live="polite">
        <h2
          className="product-name"
          style={{ color: active.accent }}
        >
          {active.name}
        </h2>
        <p className="product-desc">{active.description}</p>
      </div>

      {/* Dot indicators */}
      <div className="dots" role="tablist" aria-label="Controles del carrusel">
        {products.map((_, i) => (
          <button
            key={i}
            className={`dot ${i === activeIndex ? "dot-active" : ""}`}
            style={i === activeIndex ? { background: active.accent } : {}}
            onClick={() => setActiveIndex(i)}
            role="tab"
            aria-selected={i === activeIndex}
            aria-label={`Ver producto ${i + 1}`}
          />
        ))}
      </div>

      {/* Price badge */}
      <div className="price-section">
        <div className="price-divider">
          <span className="diamond">♦</span>
          <div className="divider-line" />
        </div>

        <div className="price-pill">
          <span className="price-amount">{active.price} C/U</span>
        </div>

        <div className="price-divider">
          <div className="divider-line" />
          <span className="diamond">♦</span>
        </div>
      </div>

      <p className="promo-tag">COMPRA 1 LLEVA 2</p>
    </div>
  );
}
