import type { NextConfig } from "next";
import path from "path";

const nextConfig: NextConfig = {
  output: "standalone",   // 🔴 REQUIRED for Docker / AKS
  turbopack: {
    root: path.join(__dirname),
  },
};

export default nextConfig;
