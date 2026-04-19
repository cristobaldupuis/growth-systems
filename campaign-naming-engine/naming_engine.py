import datetime

class GrowthNamingEngine:
    """
    Standardized Naming Engine for Multi-Brand Portfolio.
    Designed to maintain Data Fabric integrity for automated reporting.
    """
    
    # Schemas based on Cristobal's established conventions
    SCHEMAS = {
        "META_PROSP": ["Channel", "Geo", "Funnel", "Objective", "Audience", "Placement", "CampaignID"],
        "META_INFLUENCER": ["Channel", "Handle", "Asset", "Campaign", "Gender", "Theme", "Category", "Flavor", "Length"],
        "GOOGLE_SEARCH": ["Channel", "Geo", "Funnel", "Objective", "Audience", "Placement", "CampaignID"]
    }

    def __init__(self, brand_prefix="CSC"):
        self.brand = brand_prefix

    def generate_campaign_name(self, schema_type, data):
        """Generates a standardized campaign string."""
        if schema_type not in self.SCHEMAS:
            raise ValueError(f"Schema {schema_type} not recognized.")
        
        schema = self.SCHEMAS[schema_type]
        components = [data.get(field, "NA") for field in schema]
        
        # Consistent joining with underscores for machine-readability
        campaign_string = "_".join(components)
        return f"{self.brand}_{campaign_string}"

    def generate_utm_string(self, base_url, source, medium, campaign_name, content):
        """Automates UTM construction to prevent manual entry errors."""
        query_params = {
            "utm_source": source.lower(),
            "utm_medium": medium.lower(),
            "utm_campaign": campaign_name,
            "utm_content": content.replace(" ", "-")
        }
        params_string = "&".join([f"{k}={v}" for k, v in query_params.items()])
        return f"{base_url}?{params_string}"

# --- EXAMPLE USAGE (Inspired by Cristobal's Netshoes & Legendary Data) ---

engine = GrowthNamingEngine(brand_prefix="LEGENDARY")

# Example 1: Meta Influencer Campaign (as seen in Sheet1)
meta_influencer_data = {
    "Channel": "Meta", "Handle": "Col", "Asset": "EmmaBrune", "Campaign": "R3",
    "Gender": "F", "Theme": "Gym-Protein", "Category": "Pastry", 
    "Flavor": "Chocolate", "Length": "35s-Raw"
}
camp_name = engine.generate_campaign_name("META_INFLUENCER", meta_influencer_data)

# Output for GitHub Portfolio
print(f"Generated Campaign Name: {camp_name}")
# Output: LEGENDARY_Meta_Col_EmmaBrune_R3_F_Gym-Protein_Pastry_Chocolate_35s-Raw

print(f"Generated UTM: {engine.generate_utm_string('https://legendaryfoods.com', 'facebook', 'paid_social', camp_name, '35s-Raw')}")
