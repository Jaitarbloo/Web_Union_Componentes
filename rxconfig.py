
import reflex as rx

config = rx.Config( 
    
                app_name="Web_Union_componentes",
                cors_allouwed_origins=["https://api.zabalgana.com", "https://localhost:3000"],
                disable_plugins=["reflex.plugins.sitemap.SitemapPlugin"]
                                       
                    )