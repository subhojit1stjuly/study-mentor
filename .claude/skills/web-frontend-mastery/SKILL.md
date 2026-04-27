---
name: web-frontend-mastery
description: "Use when: studying web frontend development, learning HTML CSS JavaScript, learning React Vue Angular, understanding responsive design, studying web accessibility a11y, learning TypeScript, studying browser APIs, understanding DOM manipulation, learning CSS frameworks Tailwind Bootstrap, studying web performance, learning frontend testing, building web applications, studying frontend architecture."
argument-hint: "Topic or phase (e.g., 'React hooks', 'CSS Grid', 'Phase 2 React')"
---

# Web Frontend Mastery Roadmap

A structured roadmap for mastering modern web frontend development — from HTML/CSS fundamentals through production-grade React/Vue/Angular applications.

## When to Use

- Starting or resuming a frontend learning journey
- Learning HTML, CSS, JavaScript, TypeScript
- Mastering a frontend framework (React, Vue, Angular)
- Understanding web performance and accessibility
- Building portfolio-worthy web projects

---

## Phase 0: Web Fundamentals

> **Goal**: Master the building blocks of the web.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | HTML5 | Semantic HTML, forms, validation, media elements, canvas, SVG, SEO basics, meta tags, Open Graph |
| 0.2 | CSS3 Foundations | Selectors, specificity, box model, display (block, inline, flex, grid), positioning, z-index, cascade, inheritance |
| 0.3 | CSS Layout | Flexbox (all properties, patterns), CSS Grid (template areas, auto-fit/fill, named lines), responsive design (media queries, mobile-first) |
| 0.4 | CSS Advanced | Animations/transitions, custom properties (CSS variables), pseudo-elements/classes, gradients, shadows, filters, clipping/masking |
| 0.5 | CSS Architecture | BEM methodology, CSS Modules, CSS-in-JS concepts, Tailwind CSS utility-first approach, design system token structure |

### Checkpoint
- Build a responsive landing page with Flexbox and Grid (no framework)
- Explain the CSS specificity hierarchy
- Create a CSS animation without JavaScript

---

## Phase 1: JavaScript Mastery

> **Goal**: Deep understanding of JavaScript — the language, not just the syntax.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | JS Fundamentals | Variables (var/let/const), types, type coercion, equality (== vs ===), scope (block, function, global), hoisting |
| 1.2 | Functions & Closures | Function declarations/expressions, arrow functions, closures, IIFE, higher-order functions, callbacks, `this` binding (call, apply, bind) |
| 1.3 | Objects & Prototypes | Object creation patterns, prototypal inheritance, `__proto__` vs prototype, classes (ES6+), getters/setters, property descriptors |
| 1.4 | Async JavaScript | Event loop, call stack, microtask/macrotask queues, callbacks, Promises (then/catch/finally, Promise.all/race/allSettled), async/await, error handling |
| 1.5 | DOM & Browser APIs | DOM traversal/manipulation, event handling (bubbling, capturing, delegation), Intersection Observer, MutationObserver, Web Storage, Fetch API |
| 1.6 | ES6+ Features | Destructuring, spread/rest, template literals, modules (import/export), iterators/generators, Map/Set/WeakMap/WeakSet, optional chaining, nullish coalescing |
| 1.7 | TypeScript | Types, interfaces, generics, enums, type narrowing, utility types (Partial, Pick, Omit, Record), declaration files, strict mode |

### Checkpoint
- Explain the event loop with a concrete example (setTimeout vs Promise ordering)
- Implement a debounce/throttle function from scratch
- Build a small app using only vanilla JS + DOM APIs

---

## Phase 2: React (Primary Framework)

> **Goal**: Master React from fundamentals through advanced patterns.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | React Fundamentals | JSX, components (functional), props, state (useState), conditional rendering, lists & keys, event handling |
| 2.2 | Hooks Deep Dive | useState, useEffect (cleanup, dependencies), useContext, useRef, useMemo, useCallback, useReducer, custom hooks |
| 2.3 | State Management | Local state, lifting state, Context API, Redux Toolkit (slices, thunks, RTK Query), Zustand, Jotai — when to use what |
| 2.4 | Routing & Navigation | React Router v6 (routes, params, nested routes, loaders, actions), protected routes, navigation patterns |
| 2.5 | Data Fetching | useEffect + fetch, React Query/TanStack Query (caching, stale time, mutations, infinite queries), SWR, error/loading states |
| 2.6 | Forms | Controlled vs uncontrolled, React Hook Form, Zod/Yup validation, multi-step forms, file uploads |
| 2.7 | Styling | CSS Modules, Tailwind CSS, styled-components, Emotion, design system components, responsive patterns |
| 2.8 | Advanced Patterns | Render props, compound components, higher-order components, portal, error boundaries, suspense, lazy loading, code splitting |

### Projects
- Todo app (CRUD with local state)
- Dashboard with data fetching, charts, and routing
- Full-stack app with authentication

---

## Phase 3: Frontend Engineering

> **Goal**: Production-grade frontend skills.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Testing | Unit tests (Jest, Vitest), component tests (React Testing Library), integration tests, E2E tests (Playwright, Cypress), test strategy |
| 3.2 | Performance | Core Web Vitals (LCP, FID, CLS), bundle analysis, code splitting, lazy loading, memoization, virtual lists, image optimization |
| 3.3 | Accessibility (a11y) | WCAG 2.1 guidelines, ARIA roles/attributes, keyboard navigation, screen reader testing, focus management, color contrast |
| 3.4 | Build Tools | Vite, Webpack basics, Babel, ESLint, Prettier, module bundling, tree shaking, HMR, environment variables |
| 3.5 | Next.js / SSR | Server-side rendering, static site generation, ISR, App Router, Server Components, API routes, middleware, deployment |
| 3.6 | Security | XSS prevention in React, CSRF tokens, CSP headers, dependency auditing, secure cookie handling, CORS |

---

## Phase 4: Alternative Frameworks (Breadth)

> **Goal**: Understand alternatives to expand versatility.

| Framework | Key Concepts to Learn |
|-----------|---------------------|
| Vue 3 | Composition API, reactivity (ref/reactive), Vuex/Pinia, Vue Router, SFC, Nuxt.js |
| Angular | Modules, components, services, dependency injection, RxJS, NgRx, Angular CLI |
| Svelte | Reactive declarations, stores, SvelteKit, compiled approach, no virtual DOM |

---

## Progress Tracking

- Save notes under `web-dev/frontend/` folder
- Create `web-dev/frontend/progress.md` to track completed modules
- Save project code under `web-dev/projects/`

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| MDN Web Docs | Reference | HTML/CSS/JS reference |
| javascript.info | Tutorial | Deep JavaScript learning |
| React Docs (react.dev) | Docs | Official React learning |
| Frontend Masters | Course | Comprehensive frontend courses |
| web.dev (Google) | Reference | Web performance & best practices |
| Kent C. Dodds Blog | Blog | React patterns & testing |
