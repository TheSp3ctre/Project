import Link from "next/link"
import { ShoppingBag } from 'lucide-react'

export function SiteHeader() {
  return (
    <header className="w-full py-4 px-6 bg-[#e6f7ef]">
      <div className="container flex items-center justify-between">
        <Link href="/" className="text-[#1a472a] text-xl font-serif">
          Fratello D&apos;Affari
        </Link>
        <nav className="flex items-center space-x-8">
          <Link href="#" className="text-[#1a472a] text-sm uppercase">
            Casa
          </Link>
          <Link href="#" className="text-[#1a472a] text-sm uppercase">
            Loja
          </Link>
          <Link href="#" className="text-[#1a472a] text-sm uppercase">
            Produtos
          </Link>
          <Link href="#" className="text-[#1a472a] text-sm uppercase">
            Contato
          </Link>
          <Link href="#" className="text-[#1a472a]">
            <ShoppingBag className="h-5 w-5" />
          </Link>
          <button className="text-[#1a472a] text-sm uppercase border border-[#1a472a] px-4 py-1 rounded">
            Login
          </button>
        </nav>
      </div>
    </header>
  )
}

