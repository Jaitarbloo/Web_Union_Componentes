"""
import reflex as rx

config = rx.Config( 
    
                app_name="Web_Union_componentes",
                api_urls=["https://web-union-componentes.onrender.com", "https://localhost:3000", "https://api.zabalgana.com/"],
                disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
                                       
                    )
"""

import reflex as rx

config = rx.Config(
    app_name="Web_Union_componentes",
    cors_allowed_origins=[
        "https://www.zabalgana.com",   # Frontend desplegado en Vercel
        "https://api.zabalgana.com",   # Backend desplegado en Render
        "http://localhost:3000"        # Desarrollo local
    ],
    disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]  
)
