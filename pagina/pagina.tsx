import { SiteHeader } from "@/components/site-header"
import { HeroSection } from "@/components/hero-section"

export default function Home() {
  return (
    <div className="min-h-screen bg-[#e6f7ef]">
      <SiteHeader />
      <HeroSection />
    </div>
  )
}

