import 'package:flutter/material.dart';

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('个人中心')),
      body: Column(
        children: [
          Container(
            padding: EdgeInsets.all(20),
            child: Row(
              children: [
                CircleAvatar(radius: 40, child: Icon(Icons.person, size: 50)),
                SizedBox(width: 20),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('载堉 (Admin)', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
                    Text('出海赛道资深企业家', style: TextStyle(color: Colors.grey)),
                  ],
                )
              ],
            ),
          ),
          Divider(),
          ListTile(
            leading: Icon(Icons.favorite, color: Colors.red),
            title: Text('我的收藏'),
            trailing: Icon(Icons.chevron_right),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.description, color: Colors.blue),
            title: Text('已生成的报告'),
            trailing: Icon(Icons.chevron_right),
            onTap: () {},
          ),
          ListTile(
            leading: Icon(Icons.settings, color: Colors.grey),
            title: Text('设置'),
            trailing: Icon(Icons.chevron_right),
            onTap: () {},
          ),
          Spacer(),
          Padding(
            padding: EdgeInsets.all(20),
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(primary: Colors.redAccent, minimumSize: Size(double.infinity, 50)),
              onPressed: () => Navigator.pop(context),
              child: Text('退出登录'),
            ),
          )
        ],
      ),
    );
  }
}
