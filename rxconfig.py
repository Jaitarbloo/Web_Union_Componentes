
import reflex as rx

config = rx.Config( 
    
                app_name="Web_Union_componentes",
                cors_allowed_origins=["https://web-union-componentes.onrender.com", "https://localhost:3000"],
                disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
                                       
                    )