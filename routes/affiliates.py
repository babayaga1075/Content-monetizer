from flask import Blueprint, request, jsonify

affiliates_bp = Blueprint('affiliates', __name__)

# Sample data structure for affiliate links
affiliate_links = []

@affiliates_bp.route('/affiliates', methods=['POST'])
def add_affiliate():
    """Add a new affiliate link."""
    data = request.json
    link = data.get('link')
    description = data.get('description')
    if not link or not description:
        return jsonify({'error': 'Link and description are required'}), 400
    affiliate_links.append({'link': link, 'description': description})
    return jsonify({'message': 'Affiliate link added', 'link': link}), 201

@affiliates_bp.route('/affiliates', methods=['GET'])
def get_affiliates():
    """Get all affiliate links."""
    return jsonify(affiliate_links), 200

@affiliates_bp.route('/affiliates/conversion', methods=['POST'])
def track_conversion():
    """Track a conversion for an affiliate link."""
    data = request.json
    link = data.get('link')
    if link not in [affiliate['link'] for affiliate in affiliate_links]:
        return jsonify({'error': 'Affiliate link not found'}), 404
    # Here you could implement conversion tracking logic
    return jsonify({'message': 'Conversion tracked for link', 'link': link}), 200

