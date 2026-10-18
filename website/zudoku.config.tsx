
import type { ZudokuConfig } from "zudoku";

const config: ZudokuConfig = {
  basePath: "/rental-api",
  site: {
    logo: {
      src: { light: "/logo-light.svg", dark: "/logo-dark.svg" },
      alt: "RentAI API",
      width: "130px",
    },
  },
  docs: {
    files: "./pages/**/*.{md,mdx}",
  },
  navigation: [
    {
      type: "category",
      label: "Documentation",
      items: [
        {
          type: "doc",
          file: "installation.md",
          label: "Installation",
        },
        {
          type: "doc",
          file: "authorization.md",
          label: "Authorization",
        },
        {
          type: "doc",
          file: "about.md",
          label: "About",
        },
      ],
    },
    {
      type: "link",
      to: "/api",
      label: "API Reference",
    },
    {
      type: "link",
      to: "/about",
      label: "About",
    },
  ],
  redirects: [{ from: "/", to: "/installation" }],
  apis: [
    {
      type: "file",
      input: "./apis/openapi.yaml",
      path: "/api",
    },
  ],
};

export default config;
