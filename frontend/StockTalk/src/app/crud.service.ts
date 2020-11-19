import { Injectable } from '@angular/core';
import { User, Profile } from './Interfaces';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Router } from '@angular/router';
 
@Injectable({
  providedIn: 'root'
})

export class CrudService {

  readonly APIUrl = "http://127.0.0.1:8000";
  readonly PhotoUrl = "http://127.0.0.1:8000/media/";
  
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  }
  
  constructor(private httpClient: HttpClient, private router: Router) { }

  private instanceOfObj(object : any) {
    return object.Type;
  }

  getAll<T>(type : string): Observable<T[]> {
    return this.httpClient.get<T[]>(this.APIUrl + type)
  }

  uploadProfilePic(val:any) {
    return this.httpClient.post(this.APIUrl + '/SaveProfilePic/', val);
  }

  uploadPostPic(val:any) {
    return this.httpClient.post(this.APIUrl + '/SavePostPic/', val);
  }

  getProfile(val: any): Observable<Profile> {
    return this.httpClient.get<Profile>(this.APIUrl + "/profile/" + val);
  }

  getUser(val: any): Observable<User> {
    return this.httpClient.get<User>(this.APIUrl + "/user/" + val);
  }

  getPostList():Observable<any[]>{
    return this.httpClient.get<any[]>(this.APIUrl + '/posts/');

  }

  addPost(val: any) {
    let body = JSON.stringify(val);
    alert(body);
    return this.httpClient.post<any>(this.APIUrl + "/posts/", val);
  }

  addUser(val: any) {
      let body = JSON.stringify(val);
      return this.httpClient.post<any>(this.APIUrl + "/user/", val);
  }

  addProfile(val: any) {
    let body = JSON.stringify(val);
    return this.httpClient.post<any>(this.APIUrl + "/profile/", val);
  }

  validateUser(loginData: any) {
    let body = JSON.stringify(loginData);
    return this.httpClient.post<any>(this.APIUrl + "/login/", body);
  }

  getUserById<T>(id : Number, type : T) : Observable<T> {

    var typeStr = this.instanceOfObj(type);

    return this.httpClient.get<T>(this.APIUrl + typeStr + id, this.httpOptions);
  }

  updateUser(val:any) {
    return this.httpClient.put(this.APIUrl + '/user/', val);
  }

  updatePost(val:any) {
    return this.httpClient.put(this.APIUrl + '/posts/', val);
  }

  updateProfile(val:any) {
    return this.httpClient.put(this.APIUrl + '/profile/', val);
  }

  deleteAccount(userID: Number) {
    return this.httpClient.delete(this.APIUrl + "/delete-user/" + userID);
  }

  deleteUser<T>(id : Number, type : T): Observable<T> {

    var typeStr = this.instanceOfObj(type);

    return this.httpClient.delete<T>(this.APIUrl + typeStr + id, this.httpOptions);
  }
}
