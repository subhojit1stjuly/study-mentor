---
name: mobile-mastery
description: "Use when: studying mobile development, learning React Native, learning Flutter, building mobile apps, studying iOS development, studying Android development, learning mobile UI design, understanding mobile architecture, cross-platform development, mobile testing, publishing apps to App Store Google Play, mobile performance optimization."
argument-hint: "Topic or phase (e.g., 'React Native navigation', 'Flutter widgets', 'Phase 2')"
---

# Mobile Development Mastery Roadmap

A structured roadmap for mastering mobile development — covering cross-platform (React Native, Flutter) and native approaches.

## When to Use

- Starting or resuming a mobile development journey
- Building mobile applications (iOS, Android, cross-platform)
- Learning React Native or Flutter
- Understanding mobile architecture patterns
- Preparing for mobile developer interviews

---

## Phase 0: Mobile Fundamentals

> **Goal**: Understand how mobile apps work the platform landscape.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 0.1 | Mobile Landscape | Native vs cross-platform vs hybrid, iOS vs Android ecosystem, app lifecycle, platform guidelines (HIG, Material Design) |
| 0.2 | Core Concepts | Screens & navigation, UI components, layouts, responsive design, gestures & touch, local storage, permissions |
| 0.3 | Networking | REST API consumption, authentication, image loading & caching, offline-first patterns, WebSocket for real-time |

---

## Phase 1: React Native (Cross-Platform)

> **Goal**: Build production-quality mobile apps with React Native.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 1.1 | RN Fundamentals | Components (View, Text, Image, ScrollView, FlatList), StyleSheet, Flexbox layout, platform-specific code |
| 1.2 | Navigation | React Navigation (stack, tab, drawer), deep linking, navigation state, passing params, nested navigators |
| 1.3 | State Management | useState/useReducer, Context, Redux Toolkit, Zustand, React Query/TanStack Query for server state |
| 1.4 | Native Features | Camera, geolocation, push notifications, biometrics, file system, device sensors, permissions handling |
| 1.5 | UI & Animation | Animated API, Reanimated, gesture handler, Lottie animations, custom components, theming |
| 1.6 | Data & Storage | AsyncStorage, MMKV, SQLite (Expo SQLite), Realm, secure storage (Keychain/Keystore) |

### Projects
- Todo app with local storage and animations
- Social media app with feed, profiles, and real-time chat
- E-commerce app with payment integration

---

## Phase 2: Flutter (Alternative Cross-Platform)

> **Goal**: Understand Flutter to broaden cross-platform skills.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 2.1 | Dart Language | Types, null safety, async/await, streams, collections, classes, mixins, extension methods |
| 2.2 | Flutter Fundamentals | Widget tree, StatelessWidget vs StatefulWidget, BuildContext, MaterialApp, Scaffold, common widgets |
| 2.3 | Layout & UI | Row, Column, Stack, Container, Expanded, Flexible, ListView, GridView, Slivers, custom painting |
| 2.4 | State Management | setState, Provider, Riverpod, BLoC pattern, state management comparison |
| 2.5 | Navigation | Navigator 2.0, GoRouter, named routes, deep linking, bottom navigation |
| 2.6 | Platform Integration | Platform channels, plugins, camera, maps, Firebase integration, push notifications |

---

## Phase 3: Production Mobile Engineering

> **Goal**: Ship and maintain production mobile apps.

### Modules

| # | Module | Key Topics |
|---|--------|-----------|
| 3.1 | Architecture | MVVM, Clean Architecture, repository pattern, dependency injection, feature-first folder structure |
| 3.2 | Testing | Unit tests, widget/component tests, integration tests, E2E tests (Detox, Maestro), snapshot testing |
| 3.3 | Performance | JS thread vs UI thread (RN), frame rate optimization, memory leaks, image optimization, bundle size, lazy loading |
| 3.4 | CI/CD | Fastlane, GitHub Actions for mobile, code signing, beta distribution (TestFlight, Firebase App Distribution) |
| 3.5 | Publishing | App Store guidelines, Google Play requirements, app signing, versioning, release management, app review process |
| 3.6 | Analytics & Monitoring | Firebase Analytics, crash reporting (Crashlytics, Sentry), performance monitoring, A/B testing |

---

## Progress Tracking

- Save notes under `mobile-dev/` folder
- Create `mobile-dev/progress.md` to track completed modules
- Save project code under `mobile-dev/projects/`

## Recommended Resources

| Resource | Type | Best For |
|----------|------|----------|
| React Native Docs | Docs | Official RN reference |
| Flutter Docs | Docs | Official Flutter reference |
| Expo Docs | Docs | Managed RN workflow |
| William Candillon (YouTube) | Video | RN animations |
| Flutter Widget of the Week | Video | Flutter widget catalog |
| The Complete Flutter Development Bootcamp | Course | Flutter comprehensive |
