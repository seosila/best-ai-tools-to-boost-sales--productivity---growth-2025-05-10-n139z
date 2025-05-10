# Best AI Tools Directory 🚀

> Explore the Best AI Tools to Boost Your Sales & Workflow - A comprehensive directory of AI-powered solutions for business growth and productivity.

[![Netlify Status](https://api.netlify.com/api/v1/badges/your-badge-id/deploy-status)](https://app.netlify.com/sites/your-site/deploys)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Directory Structure](#directory-structure)
- [Customization Guide](#customization-guide)
- [Deployment](#deployment)
- [Custom Domain Setup](#custom-domain-setup)
- [Troubleshooting](#troubleshooting)
- [Resources & Support](#resources--support)

## Overview

This directory website showcases a curated collection of AI tools organized in a responsive 3-column grid layout. Each tool entry includes key information such as name, description, pricing, and category tags.

## Features

- 🎯 Responsive 3-column grid layout
- 🏷️ Category-based filtering
- 🔍 Search functionality
- 💨 Fast loading performance
- 📱 Mobile-friendly design
- 🎨 Customizable styling
- 📊 SEO optimized

## Getting Started

### Prerequisites
- Node.js (v14 or higher)
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/ai-tools-directory.git

# Navigate to project directory
cd ai-tools-directory

# Install dependencies
npm install

# Start development server
npm run dev
```

## Directory Structure

```
ai-tools-directory/
├── src/
│   ├── data/
│   │   ├── tools.json
│   │   └── categories.json
│   ├── components/
│   │   ├── Card.js
│   │   ├── Grid.js
│   │   └── Hero.js
│   ├── styles/
│   │   └── main.css
│   └── pages/
├── public/
│   └── images/
├── package.json
└── README.md
```

## Customization Guide

### Adding/Editing Directory Items

1. Navigate to `src/data/tools.json`
2. Add new tools using the following format:

```json
{
  "id": "tool-name",
  "name": "Tool Name",
  "description": "Tool description goes here",
  "category": ["category1", "category2"],
  "pricing": "Free/Paid",
  "url": "https://toolwebsite.com",
  "image": "/images/tool-image.png"
}
```

### Modifying Category Labels

1. Open `src/data/categories.json`
2. Edit categories using this structure:

```json
{
  "categories": [
    {
      "id": "category-id",
      "name": "Category Name",
      "description": "Category description"
    }
  ]
}
```

### Updating Hero Section

1. Locate `src/components/Hero.js`
2. Modify the content:

```jsx
export default function Hero() {
  return (
    <div className="hero">
      <h1>Your Custom Title</h1>
      <p>Your custom description</p>
    </div>
  )
}
```

### Customizing Colors and Styling

1. Navigate to `src/styles/main.css`
2. Update the CSS variables:

```css
:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  --background-color: #ffffff;
  --text-color: #333333;
}
```

## Deployment

### Netlify Deployment

1. Push your code to GitHub
2. Log in to Netlify
3. Click "New site from Git"
4. Select your repository
5. Configure build settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
6. Click "Deploy site"

## Custom Domain Setup

1. Purchase a domain from your preferred registrar
2. In Netlify:
   - Go to Site settings > Domain management
   - Click "Add custom domain"
   - Enter your domain name
3. Update DNS settings:
   - Add CNAME record pointing to your Netlify URL
   - Add A record if using apex domain

## Troubleshooting

### Common Issues

**Build Failures**
- Verify Node.js version
- Check for missing dependencies
- Validate JSON syntax in data files

**Styling Issues**
- Clear browser cache
- Check CSS specificity
- Verify media query breakpoints

## Resources & Support

- [Documentation Wiki](https://github.com/yourusername/ai-tools-directory/wiki)
- [Issue Tracker](https://github.com/yourusername/ai-tools-directory/issues)
- [Contributing Guidelines](CONTRIBUTING.md)

### Community
- [Discord Server](https://discord.gg/yourserver)
- [Twitter](https://twitter.com/yourhandle)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [Your Name](https://yourwebsite.com)