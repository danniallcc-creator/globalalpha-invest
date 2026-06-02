import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ChatScreen extends StatefulWidget {
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _controller = TextEditingController();
  final List<Map<String, String>> _messages = [
    {'role': 'ai', 'text': '您好！我是您的出海助手。您可以问我关于行业合规或选品趋势的问题。'}
  ];

  void _handleSend() async {
    final text = _controller.text;
    if (text.isEmpty) return;
    setState(() {
      _messages.add({'role': 'user', 'text': text});
      _controller.clear();
    });
    
    final reply = await ApiService.postAiChat(text);
    setState(() {
      _messages.add({'role': 'ai', 'text': reply});
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('AI 智库助手')),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final msg = _messages[index];
                final isAi = msg['role'] == 'ai';
                return Align(
                  alignment: isAi ? Alignment.centerLeft : Alignment.centerRight,
                  child: Container(
                    margin: EdgeInsets.symmetric(vertical: 8),
                    padding: EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: isAi ? Colors.white10 : Colors.blueAccent.withOpacity(0.3),
                      borderRadius: BorderRadius.circular(15),
                    ),
                    child: Text(msg['text']!, style: TextStyle(fontSize: 15)),
                  ),
                );
              },
            ),
          ),
          Padding(
            padding: EdgeInsets.all(16),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(hintText: '输入咨询内容...', border: OutlineInputBorder(borderRadius: BorderRadius.circular(30))),
                  ),
                ),
                SizedBox(width: 8),
                IconButton(icon: Icon(Icons.send, color: Colors.blueAccent), onPressed: _handleSend),
              ],
            ),
          )
        ],
      ),
    );
  }
}
