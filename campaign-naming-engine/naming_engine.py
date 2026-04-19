import datetime

class GrowthNamingEngine:
    """
    Standardized Naming Engine for Multi-Brand Portfolio.
    Designed to maintain Data Fabric integrity for automated reporting.
    """
    
    # Schemas based on standardized retail conventions
    SCHEMAS = {
        "PAID_SOCIAL_PROSP": ["Channel", "Geo", "Funnel", "Objective", "Audience", "Placement", "CampaignID"],
        "INFLUENCER_UGC": ["Channel", "CreatorID", "AssetType", "Batch", "Gender", "Theme", "ProductCat", "Variant", "Length"],
        "PAID_SEARCH": ["Channel", "Geo", "Funnel", "Match_Type", "Category", "AdStyle"]
    }

    def __init__(self, brand_prefix="GEN"):
        self.brand = brand_prefix

    def generate_campaign_name(self, schema_type, data):
        """Generates a standardized campaign string."""
        if schema_type not in self.SCHEMAS:
            raise ValueError(f"Schema {schema_type} not recognized.")
        
        schema = self.SCHEMAS[schema_type]
        components = [str(data.get(field, "NA")) for field in schema]
        
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

# --- ANONYMIZED EXAMPLE USAGE ---

# Example: National Retail Launch for a Portfolio Brand
engine = GrowthNamingEngine(brand_prefix="RETAIL_X")

launch_data = {
    "Channel": "Meta", 
    "Geo": "US", 
    "Funnel": "Pros", 
    "Objective": "Conversion", 
    "Audience": "Interest-HighIncome", 
    "Placement": "AdvantagePlus", 
    "CampaignID": "L01"
}

camp_name = engine.generate_campaign_name("PAID_SOCIAL_PROSP", launch_data)

print(f"Generated Campaign Name: {camp_name}")
# Output: RETAIL_X_Meta_US_Pros_Conversion_Interest-HighIncome_AdvantagePlus_L01

print(f"Standardized UTM: {engine.generate_utm_string('https://brand-x.com', 'facebook', 'paid_social', camp_name, 'Hero-Video-V1')}")
