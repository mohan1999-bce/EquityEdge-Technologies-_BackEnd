from flask import Blueprint,jsonify, request
from App.Services.investment_dao import get_investments_by_portfolio, sell
from App.Models.portfolio import Portfolio

investment_bp = Blueprint('investment', __name__)

@investment_bp.route('/get-all/<int:portfolioId>')
def get_all_investments_by_portId(portfolioId):
    try:
        # First check if portfolio exists
        portfolio = Portfolio.query.get(portfolioId)
        if not portfolio:
            return jsonify({"message": f"Portfolio with ID {portfolioId} not found"}), 404
            
        investments = get_investments_by_portfolio(portfolioId)
        investments_dict = [investment.to_dict() for investment in investments]
        return jsonify(investments_dict), 200
    except Exception as e:
        return jsonify({"message": f"Failed to get investments of portfolio with ID {portfolioId}. Details: {str(e)}"}), 500
    
@investment_bp.route('/sell', methods = ['POST'])
def sell_investment():
    try:
        sell_json = request.get_json()
        sell(sell_json.get('investmentId'),sell_json.get('qty'), sell_json.get('price'))
        return '', 200
    except Exception as e:
        return jsonify({"message": f"Failed to sell investment {str(e)}"}), 500