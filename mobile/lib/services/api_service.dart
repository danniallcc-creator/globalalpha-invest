import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl = 'http://localhost:8000/api';

  static Future<Map<String, dynamic>> fetchMarketData() async {
    final response = await http.get(Uri.parse('$baseUrl/market'));
    return jsonDecode(response.body);
  }

  static Future<Map<String, dynamic>> fetchCompass(String category) async {
    final response = await http.get(Uri.parse('$baseUrl/compass?category=$category'));
    return jsonDecode(response.body);
  }

  static Future<List<dynamic>> fetchCompliance(String query) async {
    final response = await http.get(Uri.parse('$baseUrl/compliance?q=$query'));
    return jsonDecode(response.body);
  }

  static Future<String> postAiChat(String message) async {
    final response = await http.post(
      Uri.parse('$baseUrl/ai-chat'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'message': message}),
    );
    final data = jsonDecode(response.body);
    return data['reply'];
  }
}
